from rest_framework import viewsets

from .models import Animal
from users import permissions as user_permissions
from .serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer

    def get_permissions(self):
        if self.action in ('destroy', 'update', 'partial_update', 'create',):
            return [user_permissions.AdminPermission()]
        return super().get_permissions()

    def get_queryset(self):
        return Animal.objects.filter(organization=self.request.user.organization)
