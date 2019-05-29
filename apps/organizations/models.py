from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Organization(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True
    )
    phone_number = PhoneNumberField(
        null=True,
        blank=True
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    url = models.URLField(
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    logo = models.ImageField(
        upload_to='organizations/logos',
        null=True,
        blank=True
    )

    schedule_monday = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    schedule_tuesday = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    schedule_wednesday = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    schedule_thursday = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    schedule_friday = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    schedule_saturday = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    schedule_sunday = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )

    def __str__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)
