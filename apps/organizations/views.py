from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from organizations.models import Organization
from .serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny(), ]
        return super().get_permissions()
