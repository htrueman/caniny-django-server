from rest_framework import viewsets

from common_tools.mixins import BulkDeleteMixin
from common_tools.serializers import BulkDeleteSerializer
from .models import Animal
from users import permissions as user_permissions
from .serializers import AnimalSerializer


class AnimalViewSet(BulkDeleteMixin, viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ('destroy', 'update', 'partial_update', 'create',):
            return [user_permissions.AdminPermission()]
        return super().get_permissions()

    def get_queryset(self, ids=None):
        if self.action == 'bulk_delete' and ids:
            return Animal.objects.filter(
                organization=self.request.user.organization,
                id__in=ids)
        return Animal.objects.filter(organization=self.request.user.organization)

    def get_serializer_class(self):
        if self.action == 'bulk_delete':
            return BulkDeleteSerializer
        return AnimalSerializer
