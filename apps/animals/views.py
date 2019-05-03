import datetime
from copy import deepcopy

from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from rest_framework.response import Response

from common_tools.mixins import BulkDeleteMixin
from common_tools.pagination import PagePagination
from common_tools.serializers import BulkDeleteSerializer
from .models import Animal
from users import permissions as user_permissions
from .serializers import AnimalListSerializer, AnimalDetailSerializer


class AnimalFilter(filters.FilterSet):
    age = filters.NumberFilter(method='age_filter')
    age__gte = filters.NumberFilter(method='age_bound_filter')
    age__lte = filters.NumberFilter(method='age_bound_filter')

    class Meta:
        model = Animal
        fields = {
            'id': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'name': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'date_of_birth': ['exact', 'gte', 'lte'],
            'age': ['exact', 'gte', 'lte'],
            'life_stage': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'gender': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'species': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'breed__name': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'species_details': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'origin_country': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'pregnant': ['iexact'],
            'personality': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'energy_level': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'cats_friendly': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'dogs_friendly': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'animals_friendly': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'humans_friendly': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'kids_friendly': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'bites': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'for_adoption': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'for_foster': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'accommodation': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'tag_number': ['exact', 'gte', 'lte'],
            'microchip_number': ['exact', 'gte', 'lte'],
            'joined_reason': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'entry_date': ['exact', 'gte', 'lte'],
            'leave_reason': ['exact', 'gte', 'lte'],
            'leave_date': ['exact', 'gte', 'lte'],
            'history': ['exact', 'gte', 'lte'],
        }

    def age_filter(self, queryset, age, value):
        left_bound_date_of_birth = datetime.datetime.now() - relativedelta(years=+value)
        return queryset.filter(Q(age=value) | Q(date_of_birth=left_bound_date_of_birth))

    def age_bound_filter(self, queryset, age, value):
        left_bound_date_of_birth = datetime.datetime.now() - relativedelta(years=+value)
        if 'gte' in age:
            q = Q(age__gte=value) | Q(date_of_birth__gte=left_bound_date_of_birth)
        else:
            q = Q(age_lte=value) | Q(date_of_birth__lte=left_bound_date_of_birth)
        return queryset.filter(q)


class AnimalViewSet(BulkDeleteMixin, viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalFilter
    pagination_class = PagePagination
    http_method_names = ('get', 'post', 'put', 'delete', 'head', 'options',)

    def get_permissions(self):
        if self.action in ('destroy', 'update', 'create', 'bulk_delete',):
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
        elif self.action == 'list':
            return AnimalListSerializer
        return AnimalDetailSerializer

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)

    def perform_update(self, serializer):
        return serializer.save(organization=self.request.user.organization)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = self.get_object()
        old_id = deepcopy(instance.id)
        instance.delete()
        new_instance = self.perform_update(serializer)
        new_instance_id = deepcopy(new_instance.id)
        new_instance.id = old_id
        new_instance.save()
        Animal.objects.filter(id=new_instance_id).delete()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
