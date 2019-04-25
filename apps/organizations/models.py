from django.db import models


class Organization(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True
    )

    def __str__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)
