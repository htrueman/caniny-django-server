import datetime

from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        return (datetime.datetime.now() - obj.date_of_birth).days / 365.25

    def validate_date_of_birth(self, val):
        if val > datetime.datetime.now():
            raise ValidationError(_('Date of birth can\'t be in future.'))
        return val

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'species',
            'breed',
            'date_of_birth',
            'age',
            'size',
            'social',
            'accommodation',
            'tag',
            'microchip',
        )
        write_only_fields = (
            'date_of_birth',
        )
