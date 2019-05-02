from django.contrib import admin

from .models import Animal, Breed, AnimalHealth, AnimalHealthVaccination, AnimalHealthMedication, AnimalAppearance, \
    AnimalTraining, AnimalOwner

admin.site.register(Animal)
admin.site.register(AnimalHealth)
admin.site.register(AnimalHealthVaccination)
admin.site.register(AnimalHealthMedication)
admin.site.register(AnimalAppearance)
admin.site.register(AnimalTraining)
admin.site.register(AnimalOwner)
admin.site.register(Breed)
