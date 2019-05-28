from django.contrib import admin

from .models import Animal, Breed, AnimalHealth, AnimalHealthCare, AnimalAppearance, \
    AnimalTraining, AnimalOwner, AnimalTableMetadata

admin.site.register(Animal)
admin.site.register(AnimalHealth)
admin.site.register(AnimalHealthCare)
admin.site.register(AnimalAppearance)
admin.site.register(AnimalTraining)
admin.site.register(AnimalOwner)
admin.site.register(Breed)
admin.site.register(AnimalTableMetadata)
