from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .utils import account_activation_token
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


@api_view(['GET'])
def activate(request, uidb64, token, *args, **kwargs):
    try:
        user = User.objects.get(pk=uidb64)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response({'status': 'Thank you for your email confirmation. Now you can log in to your account.'})
    else:
        return Response({'status': 'Activation link is invalid!'}, status=status.HTTP_400_BAD_REQUEST)
