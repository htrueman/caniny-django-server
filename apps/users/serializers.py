from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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
