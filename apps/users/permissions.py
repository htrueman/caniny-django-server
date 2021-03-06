from rest_framework.permissions import BasePermission

from users.constants import UserTypes


class HelperPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type in [
            UserTypes.HELPER,
            UserTypes.ADMIN,
            UserTypes.SUPER_ADMIN,
            UserTypes.DJANGO_ADMIN
        ]


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type in [
            UserTypes.ADMIN,
            UserTypes.SUPER_ADMIN,
            UserTypes.DJANGO_ADMIN
        ]


class SuperAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type in [
            UserTypes.SUPER_ADMIN,
            UserTypes.DJANGO_ADMIN
        ]
