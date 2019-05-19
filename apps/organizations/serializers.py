from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
        )


class OrganizationDetailSerializer(serializers.ModelSerializer):
    logo_image = Base64ImageField(source='logo', required=False, represent_in_base64=True)

    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
            'phone_number',
            'email',
            'url',
            'address',
            'description',
            'logo_image',
        )
