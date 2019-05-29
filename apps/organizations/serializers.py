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
    logo_image = Base64ImageField(source='logo', required=False)

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

            'schedule_monday',
            'schedule_tuesday',
            'schedule_wednesday',
            'schedule_thursday',
            'schedule_friday',
            'schedule_saturday',
            'schedule_sunday',
        )
