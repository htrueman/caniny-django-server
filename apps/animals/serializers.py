import datetime
from dateutil.relativedelta import relativedelta
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    image = Base64ImageField(source='photo')

    def get_age(self, obj):
        delta = relativedelta(datetime.datetime.now(), obj.date_of_birth)
        years_ending = 's' if delta.years > 1 else ''
        months_ending = 's' if delta.months > 1 else ''
        days_ending = 's' if delta.days > 1 else ''

        return '{years} year{years_ending} {months} month{months_ending} {days} day{days_ending}'.format(
            years=delta.years,
            months=delta.months,
            days=delta.days,
            years_ending=years_ending,
            months_ending=months_ending,
            days_ending=days_ending
        )

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
            'image',
        )
        write_only_fields = (
            'date_of_birth',
        )
