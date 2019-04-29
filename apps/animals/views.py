from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django_filters import rest_framework as filters

from common_tools.mixins import BulkDeleteMixin
from common_tools.pagination import PagePagination
from common_tools.serializers import BulkDeleteSerializer
from .models import Animal
from users import permissions as user_permissions
from .serializers import AnimalSerializer


class AnimalFilter(filters.FilterSet):
    class Meta:
        model = Animal
        fields = {
            'id': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'name': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'species': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'breed': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'date_of_birth': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'size': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'social': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'accommodation': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'tag': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'microchip': ['iexact', 'icontains', 'istartswith', 'iendswith'],
        }


class AnimalViewSet(BulkDeleteMixin, viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalFilter
    pagination_class = PagePagination

    def get_permissions(self):
        if self.action in ('destroy', 'update', 'partial_update', 'create', 'bulk_delete',):
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

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)

    def perform_update(self, serializer):
        serializer.save(organization=self.request.user.organization)
