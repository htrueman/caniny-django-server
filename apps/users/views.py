from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import api_view, action
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.settings import api_settings

from .constants import UserTypes
from .utils import account_activation_token
from .serializers import UserSignUpSerializer, UserSignUpGoogleSerializer, UserSignUpFBSerializer, \
    UserSignUpIGSerializer, LoginSerializer, RequestAccessSerializer, \
    PasswordResetSendLinkSerializer, PasswordResetSerializer, UserSerializer
from . import permissions as user_permissions

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
        elif self.action == 'request_access':
            return RequestAccessSerializer
        return UserSignUpSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.user_type = UserTypes.SUPER_ADMIN
        user.save()

    def google(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def facebook(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def instagram(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def request_access(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['GET'])
@permission_classes((AllowAny,))
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
        return Response({'status': 'Activation link is not valid!'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class PasswordResetView(GenericAPIView):
    serializer_class = PasswordResetSendLinkSerializer
    permission_classes = (AllowAny,)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class ConfirmPasswordResetView(GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        try:
            user = User.objects.get(pk=kwargs['id'])
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, kwargs['token']):
            user.set_password(request.data['password_1'])
            user.save()
            return Response({'status': 'Password changed.'}, status=status.HTTP_200_OK, headers=headers)
        else:
            return Response({'status': 'Token link is not valid!'}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    def get_serializer_class(self):
        if self.action == 'change_password':
            return PasswordResetSerializer

        return UserSerializer

    def get_permissions(self):
        if self.action in ('list', 'destroy'):
            return [user_permissions.SuperAdminPermission()]
        return super().get_permissions()

    def get_queryset(self):
        return User.objects.filter(organization=self.request.user.organization)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    @action(detail=True, methods=['PATCH'])
    def change_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        request.user.set_password(request.data['password_1'])
        request.user.save()
        return Response({'status': 'Password changed.'}, status=status.HTTP_200_OK, headers=headers)
