from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from common_tools.mixins import BulkDeleteMixin
from common_tools.pagination import PagePagination
from common_tools.serializers import BulkDeleteSerializer
from .constants import UserTypes
from .utils import account_activation_token
from .serializers import UserSignUpSerializer, UserSignUpGoogleSerializer, UserSignUpFBSerializer, \
    UserSignUpIGSerializer, LoginSerializer, RequestAccessSerializer, \
    PasswordResetSendLinkSerializer, PasswordResetSerializer, UserSerializer, SuperAdminUserSerializer, \
    PasswordChangeSerializer
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


class UserFilter(filters.FilterSet):
    phone_number__iexact = filters.CharFilter(method='phone_number_filter')
    phone_number__icontains = filters.CharFilter(method='phone_number_filter')
    phone_number__istartswith = filters.CharFilter(method='phone_number_filter')
    phone_number__iendswith = filters.CharFilter(method='phone_number_filter')

    class Meta:
        model = User
        fields = {
            'first_name': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'last_name': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'phone_number': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'email': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'user_type': ['iexact'],
            'join_date': ['exact', 'gte', 'lte'],
        }

    def phone_number_filter(self, queryset, filter_key, value):
        return queryset.filter(**{filter_key: str(value)})


class UserViewSet(BulkDeleteMixin, viewsets.ModelViewSet):
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend,)
    search_fields = (
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'user_type',
        'join_date',
    )
    ordering_fields = (
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'user_type',
        'join_date',
    )
    filterset_class = UserFilter
    pagination_class = PagePagination

    def get_serializer_class(self):
        if self.action == 'change_password':
            return PasswordChangeSerializer
        elif self.action == 'bulk_delete':
            return BulkDeleteSerializer
        elif self.action in ['update', 'create', 'partial_update'] and self.request.user.user_type in [
            UserTypes.SUPER_ADMIN,
            UserTypes.DJANGO_ADMIN
        ]:
            return SuperAdminUserSerializer

        return UserSerializer

    def get_permissions(self):
        if self.action in ('destroy', 'update', 'partial_update', 'change_password', 'bulk_delete',):
            return [user_permissions.SuperAdminPermission()]
        return super().get_permissions()

    def get_queryset(self, ids=None):
        if self.action == 'bulk_delete' and ids:
            return User.objects\
                .filter(organization=self.request.user.organization, id__in=ids)\
                .exclude(id=self.request.user.id)
        return User.objects\
            .filter(organization=self.request.user.organization)\
            .exclude(id=self.request.user.id)\
            .order_by('is_active')

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def get_object(self):
        if self.kwargs.get('pk'):
            return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('pk'))
        return self.request.user

    @action(detail=True, methods=['PATCH'])
    def change_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        request.user.set_password(request.data['password_1'])
        request.user.save()
        return Response({'status': 'Password changed.'}, status=status.HTTP_200_OK, headers=headers)

    def profile_update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def profile_update_partial(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def profile_change_password(self, request, *args, **kwargs):
        return self.change_password()

    def perform_destroy(self, instance):
        if instance.is_superuser or instance.is_staff or instance.user_type == UserTypes.DJANGO_ADMIN:
            raise ValidationError({'nonFieldErrors': _('You can\'t delete this user.')})
        instance.delete()

    def perform_create(self, serializer):
        user = serializer.save()
        user.organization = self.request.user.organization
        user.save()
