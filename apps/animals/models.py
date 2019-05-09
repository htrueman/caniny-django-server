import uuid

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from . import constants

User = get_user_model()


class Breed(models.Model):
    name = models.CharField(max_length=64)
    species = models.CharField(choices=constants.Species.SPECIES, max_length=5)

    def __str__(self):
        return '{} {}'.format(self.species, self.name)


class Animal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    life_stage = models.CharField(choices=constants.LifeStages.LIFE_STAGES, null=True, blank=True, max_length=6)
    gender = models.CharField(choices=constants.Genders.GENDERS, max_length=6)
    species = models.CharField(choices=constants.Species.SPECIES, max_length=5)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    species_details = models.TextField(blank=True, null=True)
    origin_country = models.CharField(max_length=64, null=True, blank=True, choices=constants.COUNTRIES)
    pregnant = models.BooleanField(null=True, blank=True)
    personality = models.CharField(
        max_length=10,
        null=True,
        blank=False,
        choices=constants.Personalities.PERSONALITIES
    )
    energy_level = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        choices=constants.EnergyLevels.ENERGY_LEVELS
    )
    cats_friendly = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        choices=constants.CatsFriendlyChoices.CATS_FRIENDLY_CHOICES
    )
    dogs_friendly = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        choices=constants.CatsFriendlyChoices.CATS_FRIENDLY_CHOICES
    )
    animals_friendly = models.CharField(
        max_length=18,
        null=True,
        blank=True,
        choices=constants.AnimalsFriendlyChoices.ANIMALS_FRIENDLY_CHOICES
    )
    humans_friendly = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        choices=constants.HumansFriendlyChoices.HUMANS_FRIENDLY_CHOICES
    )
    kids_friendly = models.CharField(
        max_length=18,
        null=True,
        blank=True,
        choices=constants.KidsFriendlyChoices.KIDS_FRIENDLY_CHOICES
    )
    bites = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        choices=constants.BiteChoices.BITE_CHOICES
    )
    for_adoption = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        choices=constants.AdoptionChoices.ADOPTION_CHOICES
    )
    for_foster = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        choices=constants.FosterChoices.FOSTER_CHOICES
    )
    adoption_date = models.DateField(null=True, blank=True)
    fostering_date = models.DateField(null=True, blank=True)
    sheltering_background = models.TextField(null=True, blank=True)
    accommodation = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        choices=constants.Accommodations.ACCOMMODATIONS
    )
    tag_id = models.CharField(max_length=64, null=True, blank=True)
    chip_producer = models.CharField(max_length=64, null=True, blank=True)
    chip_id = models.CharField(max_length=64, null=True, blank=True)
    joined_reason = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        choices=constants.JoinedReasons.JOINED_REASONS
    )
    entry_date = models.DateField(null=True, blank=True)
    leave_reason = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        choices=constants.LeaveReasons.LEAVE_REASONS
    )
    leave_date = models.DateField(null=True, blank=True)
    history = models.TextField(null=True, blank=True)
    photo = models.ImageField(
        upload_to='animals/photos',
        null=True,
        blank=True
    )

    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {} {}'.format(self.chip_id, self.name, self.species)


class AnimalTableMetadata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    columns = ArrayField(models.CharField(max_length=10, blank=True), default=list)

    def __str__(self):
        return ', '.join(self.columns)


class AnimalHealth(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)

    height = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    length = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight_condition = models.CharField(max_length=11, null=True, blank=True)
    disabled = models.BooleanField(null=True, blank=True)
    injured = models.BooleanField(null=True, blank=True)
    cryptorchid = models.BooleanField(null=True, blank=True)
    sterilized = models.CharField(max_length=8, null=True, blank=True)
    sterilized_date = models.DateField(null=True, blank=True)
    eyes_sight = models.CharField(max_length=9, null=True, blank=True, choices=constants.EyesSights.EYES_SIGHTS)
    blind = models.CharField(max_length=7, null=True, blank=True, choices=constants.BlindChoices.BLIND_CHOICES)
    deaf = models.CharField(max_length=7, null=True, blank=True, choices=constants.DeafChoices.DEAF_CHOICES)
    teeth = models.CharField(max_length=16, null=True, blank=True, choices=constants.TeethChoices.TEETH_CHOICES)
    gums = models.CharField(max_length=16, null=True, blank=True, choices=constants.Gums.GUMS)
    describe_health = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.animal)


class AnimalHealthCare(models.Model):
    animal_health = models.ForeignKey(AnimalHealth, on_delete=models.CASCADE)
    care_type = models.CharField(max_length=11, choices=constants.CareTypes.CARE_TYPES)
    note = models.CharField(max_length=128, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.animal_health)


class AnimalHealthMedication(models.Model):
    animal_health = models.ForeignKey(AnimalHealth, on_delete=models.CASCADE)
    medication_type = models.CharField(max_length=128)
    medication_date = models.DateField()

    def __str__(self):
        return '{}'.format(self.animal_health)


class AnimalAppearance(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)

    size = models.CharField(max_length=11, choices=constants.Sizes.SIZES, null=True, blank=True)
    first_coat_color = models.CharField(max_length=6, choices=constants.CoatColors.COAT_COLORS, null=True, blank=True)
    second_coat_color = models.CharField(max_length=6, choices=constants.CoatColors.COAT_COLORS, null=True, blank=True)
    third_coat_color = models.CharField(max_length=6, choices=constants.CoatColors.COAT_COLORS, null=True, blank=True)
    coat_marks = models.CharField(max_length=8, choices=constants.CoatMarks.COAT_MARKS, null=True, blank=True)
    coat_type = models.CharField(max_length=8, choices=constants.CoatTypes.COAT_TYPES, null=True, blank=True)
    first_eye_color = models.CharField(max_length=5, choices=constants.EyeColors.EYE_COLORS, null=True, blank=True)
    second_eye_color = models.CharField(max_length=5, choices=constants.EyeColors.EYE_COLORS, null=True, blank=True)
    ears = models.CharField(max_length=8, choices=constants.EarChoices.EAR_CHOICES, null=True, blank=True)
    tail = models.CharField(max_length=6, choices=constants.TailChoices.TAIL_CHOICES, null=True, blank=True)
    describe_appearance = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.animal)


class AnimalTraining(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)

    obedience = models.CharField(
        max_length=12,
        choices=constants.ObedienceChoices.OBEDIENCE_CHOICES,
        null=True,
        blank=True
    )
    house_trained = models.BooleanField(null=True, blank=True)
    crate_trained = models.BooleanField(null=True, blank=True)
    fence_required = models.BooleanField(null=True, blank=True)
    describe_training = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.animal)


class AnimalOwner(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    owner_status = models.CharField(max_length=14, null=True, blank=True, choices=constants.OwnerChoices.OWNER_CHOICES)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField(
        null=True,
        blank=True
    )
    city = models.CharField(max_length=64, null=True, blank=True)
    state = models.CharField(max_length=64, null=True, blank=True)
    zip_code = models.CharField(max_length=64, null=True, blank=True)
    origin_country = models.CharField(max_length=64, null=True, blank=True, choices=constants.COUNTRIES)
    address = models.CharField(max_length=256, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(
        upload_to='animals/owners/profile_images',
        null=True,
        blank=True
    )
    profile_id_image = models.ImageField(
        upload_to='animals/owners/profile_id_images',
        null=True,
        blank=True
    )
