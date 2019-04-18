from django.contrib.auth import get_user_model

from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

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
