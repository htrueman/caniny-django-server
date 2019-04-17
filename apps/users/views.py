from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import UserSignUpSerializer

User = get_user_model()

class SignUpViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    http_method_names = ('post',)

    def get_serializer_class(self):
        if self.action == 'google':
            pass
        elif self.action == 'facebook':
            pass
        elif self.action == 'instagram':
            pass
        return UserSignUpSerializer
