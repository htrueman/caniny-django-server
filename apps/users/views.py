from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .serializers import UserSignUpSerializer, UserSignUpGoogleSerializer, UserSignUpFBSerializer, \
    UserSignUpIGSerializer

User = get_user_model()


class SignUpViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    http_method_names = ('post',)

    def get_serializer_class(self):
        if self.action == 'google':
            return UserSignUpGoogleSerializer
        elif self.action == 'facebook':
            return UserSignUpFBSerializer
        elif self.action == 'instagram':
            return UserSignUpIGSerializer
        return UserSignUpSerializer

    def google(self, request, *args, **kwargs):
        pass

    def facebook(self, request, *args, **kwargs):
        pass

    def instagram(self, request, *args, **kwargs):
        pass
