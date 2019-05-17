import datetime
from contextlib import suppress
from copy import deepcopy

from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter

from common_tools.mixins import BulkDeleteMixin
from common_tools.pagination import PagePagination
from common_tools.serializers import BulkDeleteSerializer
from .models import Animal, Breed, AnimalOwner
from users import permissions as user_permissions
from .serializers import AnimalListSerializer, AnimalDetailSerializer, AnimalBreedSerializer, \
    AnimalTableMetadataSerializer, AnimalTableMetadata


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
            'tag_id': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'chip_producer': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'chip_id': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'joined_reason': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'entry_date': ['exact', 'gte', 'lte'],
            'leave_reason': ['iexact', 'icontains', 'istartswith', 'iendswith'],
            'leave_date': ['exact', 'gte', 'lte'],
            'history': ['iexact', 'icontains', 'istartswith', 'iendswith'],
        }

    def age_filter(self, queryset, age, value):
        left_bound_date_of_birth = datetime.datetime.now().year - value
        return queryset.filter(Q(age=value) | Q(date_of_birth__year=left_bound_date_of_birth))

    def age_bound_filter(self, queryset, age, value):
        left_bound_date_of_birth = datetime.datetime.now().year - value
        if 'gte' in age:
            q = Q(age__gte=value) | Q(date_of_birth__year__gte=left_bound_date_of_birth)
        else:
            q = Q(age__lte=value) | Q(date_of_birth__year__lte=left_bound_date_of_birth)
        return queryset.filter(q)


class AnimalViewSet(BulkDeleteMixin, viewsets.ModelViewSet):
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend,)
    filterset_class = AnimalFilter
    pagination_class = PagePagination
    http_method_names = ('get', 'post', 'put', 'delete', 'head', 'options',)
    search_fields = (
        'name',
        'date_of_birth',
        'age',
        'life_stage',
        'gender',
        'species',
        'breed__name',
        'species_details',
        'origin_country',
        'pregnant',
        'personality',
        'energy_level',
        'cats_friendly',
        'dogs_friendly',
        'animals_friendly',
        'humans_friendly',
        'kids_friendly',
        'bites',
        'for_adoption',
        'for_foster',
        'accommodation',
        'tag_id',
        'chip_producer',
        'chip_id',
        'joined_reason',
        'entry_date',
        'leave_reason',
        'leave_date',
        'history',
        'adoption_date',
        'fostering_date',
        'sheltering_background',
    )
    ordering_fields = (
        'id',
        'name',
        'date_of_birth',
        'age',
        'life_stage',
        'gender',
        'species',
        'breed',
        'species_details',
        'origin_country',
        'pregnant',
        'personality',
        'energy_level',
        'cats_friendly',
        'dogs_friendly',
        'animals_friendly',
        'humans_friendly',
        'kids_friendly',
        'bites',
        'for_adoption',
        'for_foster',
        'accommodation',
        'tag_id',
        'chip_producer',
        'chip_id',
        'joined_reason',
        'entry_date',
        'leave_reason',
        'leave_date',
        'history',
        'image',
        'image_id',
        'adoption_date',
        'fostering_date',
        'sheltering_background',
    )

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
        old_new_insctance_id = deepcopy(new_instance.id)
        new_instance_id = deepcopy(new_instance.id)
        new_instance.id = old_id
        new_instance.save()

        with suppress(Exception):
            new_instance.animaltraining.animal = new_instance
            new_instance.animaltraining.save()

        with suppress(Exception):
            new_instance.animalhealth.animal = new_instance
            new_instance.animalhealth.save()

        with suppress(Exception):
            new_instance.animalappearance.animal = new_instance
            new_instance.animalappearance.save()

        AnimalOwner.objects.filter(animal_id=old_new_insctance_id).update(animal=new_instance)

        Animal.objects.filter(id=new_instance_id).delete()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class BreedFilter(filters.FilterSet):
    class Meta:
        model = Breed
        fields = (
            'species',
        )


class BreedListView(ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = AnimalBreedSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BreedFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if self.request.GET.get('page'):
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AnimalTableMetadataView(RetrieveUpdateAPIView):
    serializer_class = AnimalTableMetadataSerializer
    http_method_names = ('get', 'put')

    def get_object(self):
        columns = [
            'name',
            'age',
            'gender',
            'species',
            'breed',
            'human_friendly',
            'animals_friendly',
            'entry_date',
        ]
        try:
            instance = AnimalTableMetadata.objects.get(user=self.request.user)
            if not instance.columns:
                instance.columns = columns
                instance.save()
        except AnimalTableMetadata.DoesNotExist:
            instance = AnimalTableMetadata.objects.create(
                user=self.request.user,
                columns=columns
            )
        return instance
