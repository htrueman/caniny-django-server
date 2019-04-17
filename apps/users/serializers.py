from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )

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

class UserSignUpIGSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=256)

    # TODO: complete
