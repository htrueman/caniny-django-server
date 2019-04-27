import requests
from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import exceptions
from django.conf import settings

from organizations.models import Organization
from .utils import send_activation_token

User = get_user_model()


class SignUpOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'name',
        )


class UserSignUpSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(
        max_length=128,
        style={'input_type': 'password'},
        write_only=True
    )
    password_2 = serializers.CharField(
        max_length=128,
        style={'input_type': 'password'},
        write_only=True
    )
    organization_dict = SignUpOrganizationSerializer(source='organization', required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password_1',
            'password_2',
            'organization_dict',
        )
        extra_kwargs = {
            'email': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise ValidationError(_('Passwords didn\'t match.'))
        return attrs

    def create(self, validated_data):
        org_dict = validated_data.pop('organization')
        organization = Organization.objects.create(**org_dict)
        password = validated_data.pop('password_1')
        validated_data.pop('password_2')
        user = super().create(validated_data)
        user.set_password(password)
        user.is_active = False
        user.organization = organization
        user.save()

        mail_subject = 'Activate your account.'
        template_name = 'account_activation_email.html'
        send_activation_token(mail_subject, template_name, user, validated_data['email'])

        return user


class UserSocialSerializerMixin:
    def create(self, validated_data):
        org_dict = validated_data.pop('organization')
        organization = Organization.objects.create(**org_dict)
        user = super().create(validated_data)
        user.organization = organization
        user.save()
        return user


class UserSignUpFBSerializer(UserSocialSerializerMixin, serializers.ModelSerializer):
    organization_dict = SignUpOrganizationSerializer(source='organization', required=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'facebook_key',
            'organization_dict',
        )
        extra_kwargs = {
            'facebook_key': {'required': True},
        }


class UserSignUpGoogleSerializer(UserSocialSerializerMixin, serializers.ModelSerializer):
    organization_dict = SignUpOrganizationSerializer(source='organization', required=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'google_key',
            'organization_dict',
        )
        extra_kwargs = {
            'google_key': {'required': True},
        }


class UserSignUpIGSerializer(UserSocialSerializerMixin, serializers.ModelSerializer):
    instagram_code = serializers.CharField(max_length=256)
    organization_dict = SignUpOrganizationSerializer(source='organization', required=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'instagram_key',

            'instagram_code',
            'organization_dict',
        )
        extra_kwargs = {
            'first_name': {'read_only': True},
            'last_name': {'read_only': True},
            'instagram_key': {'read_only': True},
        }

    def validate(self, attrs):
        res = requests.post(
            'https://api.instagram.com/oauth/access_token',
            data={
                'client_id': settings.INSTAGRAM_CLIENT_ID,
                'client_secret': settings.INSTAGRAM_CLIENT_SECRET,
                'grant_type': 'authorization_code',
                'redirect_uri': settings.REDIRECT_URL,
                'code': attrs['instagram_code'],
            }
        )
        result_dict = res.json()

        if User.objects.filter(instagram_key=result_dict['access_token']).exists():
            raise ValidationError({'instagramKey': _('user with this instagram key already exists.')})

        full_name_list = result_dict['user']['full_name'].split()
        attrs['instagram_key'] = result_dict['access_token']
        attrs['first_name'] = full_name_list[0]
        attrs['last_name'] = full_name_list[1] if len(full_name_list) >= 2 else None

        attrs.pop('instagram_code')

        return attrs


class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('style', {})

        kwargs['style']['input_type'] = 'password'
        kwargs['write_only'] = True

        super().__init__(*args, **kwargs)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    google_key = serializers.CharField(required=False)
    instagram_key = serializers.CharField(required=False)
    facebook_key = serializers.CharField(required=False)
    password = serializers.CharField(
        max_length=128,
        style={'input_type': 'password'},
        write_only=True,
        required=False
    )

    default_error_messages = {
        'no_active_account': _('No active account found with the given credentials')
    }

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        keys = attrs.keys()
        if 'email' in keys:
            username_field = 'email'
        elif 'google_key' in keys:
            username_field = 'google_key'
        elif 'instagram_key' in keys:
            username_field = 'instagram_key'
        elif 'facebook_key' in keys:
            username_field = 'facebook_key'
        else:
            raise ValidationError(_('Provide one of the fields additional to password'))

        authenticate_kwargs = {
            'username': attrs[username_field],
            'password': attrs.get('password'),
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)
        if self.user is None or not self.user.is_active:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )
        data = dict()

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class RequestAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'description',
            'organization'
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_active = False
        user.save()
        return user


class PasswordResetSendLinkSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs['email'])
            mail_subject = 'Reset password.'
            template_name = 'reset_password_email.html'
            send_activation_token(mail_subject, template_name, user, attrs['email'])
        except User.DoesNotExist:
            pass
        return attrs


class PasswordResetSerializer(serializers.Serializer):
    password_1 = serializers.CharField(
        max_length=128,
        style={'input_type': 'password'},
        write_only=True
    )
    password_2 = serializers.CharField(
        max_length=128,
        style={'input_type': 'password'},
        write_only=True
    )

    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise ValidationError(_('Passwords didn\'t match.'))
        return attrs


class UserSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField(source='profile_image', required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'address',
            'description',
            'avatar',
            'user_type',
            'is_active',
            'join_date',
        )

class UserBulkDeleteSerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.UUIDField())


class SuperAdminUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'address',
            'description',
            'avatar',
            'user_type',
            'is_active',
            'join_date',
        )

    @staticmethod
    def set_password(user):
        user_password = get_random_string(8)
        user.set_password(user_password)
        send_mail(
            'Your Caniny password',
            'Your Caniny password is {}. Log in {}/login.'.format(user_password, settings.HOST_NAME),
            settings.DEFAULT_FROM_EMAIL,
            (user.email,)
        )

    def update(self, instance, validated_data):
        if not instance.is_active and validated_data['is_active']:
            self.set_password(instance)
        return super().update(instance, validated_data)

    def create(self, validated_data):
        instance = super().create(validated_data)
        if validated_data['is_active']:
            self.set_password(instance)
        return instance
