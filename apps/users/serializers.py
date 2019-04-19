import pdb

from django.contrib.auth import get_user_model, authenticate

from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import exceptions

from .utils import account_activation_token

User = get_user_model()


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

    class Meta:
        model = User
        fields = (
            'email',
            'password_1',
            'password_2',
        )
        extra_kwargs = {
            'email': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise ValidationError(_('Passwords didn\'t match.'))
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password_1')
        validated_data.pop('password_2')
        user = super().create(validated_data)
        user.set_password(password)
        user.is_active = False
        user.save()

        mail_subject = 'Activate your account.'
        message = render_to_string('account_activation_email.html', {
            'domain': settings.HOST_NAME,
            'uid': user.pk,
            'token': account_activation_token.make_token(user),
        })
        send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, (validated_data['email'],))

        return user


class UserSignUpFBSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'facebook_key',
        )


class UserSignUpGoogleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'google_key',
        )


class UserSignUpIGSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=256)

    # TODO: complete


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['password'] = PasswordField(required=False)

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
