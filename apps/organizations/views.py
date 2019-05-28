from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from organizations.models import Organization
from users.permissions import SuperAdminPermission
from .serializers import OrganizationSerializer, OrganizationDetailSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()

    def get_permissions(self):
        if self.action in ('retrieve', 'list',):
            return [AllowAny()]
        elif self.action in ('update', 'partial_update'):
            return [SuperAdminPermission()]
        return super().get_permissions()

    def get_object(self):
        return self.request.user.organization

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update', 'retrieve'):
            return OrganizationDetailSerializer
        return OrganizationSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if self.request.GET.get('page'):
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
