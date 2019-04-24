import uuid

from django.db import models


class Animal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    species = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    size = models.CharField(max_length=128)
    social = models.CharField(max_length=128)
    accommodation = models.CharField(max_length=256)
    tag = models.CharField(max_length=128)
    microchip = models.CharField(max_length=128)

    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {} {}'.format(self.microchip, self.name, self.species)
