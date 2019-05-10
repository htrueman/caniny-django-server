import datetime
from dateutil.relativedelta import relativedelta
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from .models import Animal, Breed, AnimalHealth, AnimalHealthCare, AnimalAppearance, \
    AnimalTraining, AnimalOwner, AnimalTableMetadata


class AnimalBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = (
            'id',
            'name',
            'species',
        )


class AnimalListSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    image = Base64ImageField(source='photo', required=False)
    image_id = Base64ImageField(source='photo_id', required=False)

    def get_age(self, obj):
        return obj.age if obj.age else relativedelta(datetime.datetime.now(), obj.date_of_birth).years

    def validate_date_of_birth(self, val):
        if val > datetime.datetime.now().date():
            raise ValidationError(_('Date of birth can\'t be in future.'))
        return val

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'date_of_birth',
            'age',
            'life_stage',
            'gender',
            'species',
            'breed',
            'species_details',
            'origin_country',
            'pregnant',
            'personality',
            'energy_level',
            'cats_friendly',
            'dogs_friendly',
            'animals_friendly',
            'humans_friendly',
            'kids_friendly',
            'bites',
            'for_adoption',
            'for_foster',
            'accommodation',
            'tag_id',
            'chip_producer',
            'chip_id',
            'joined_reason',
            'entry_date',
            'leave_reason',
            'leave_date',
            'history',
            'image',
            'image_id',
            'adoption_date',
            'fostering_date',
            'sheltering_background',
        )

        extra_kwargs = {
            'date_of_birth': {'write_only': True},
        }


class AnimalHealthCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalHealthCare
        fields = (
            'care_type',
            'note',
            'date',
        )


class AnimalHealthSerializer(serializers.ModelSerializer):
    care_values = AnimalHealthCareSerializer(source='animalhealthcare_set', many=True, required=False)

    class Meta:
        model = AnimalHealth
        fields = (
            'height',
            'length',
            'weight',
            'weight_condition',
            'disabled',
            'injured',
            'cryptorchid',
            'sterilized',
            'sterilized_date',
            'eyes_sight',
            'blind',
            'deaf',
            'teeth',
            'gums',
            'describe_health',

            'care_values',
        )


class AnimalAppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalAppearance
        fields = (
            'size',
            'first_coat_color',
            'second_coat_color',
            'third_coat_color',
            'coat_marks',
            'coat_type',
            'first_eye_color',
            'second_eye_color',
            'ears',
            'tail',
            'describe_appearance',
        )


class AnimalTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalTraining
        fields = (
            'obedience',
            'house_trained',
            'crate_trained',
            'fence_required',
            'describe_training',
        )


class AnimalOwnerSerializer(serializers.ModelSerializer):
    profile_image_base = Base64ImageField(source='profile_image', required=False)
    profile_id_image_base = Base64ImageField(source='profile_id_image', required=False)

    class Meta:
        model = AnimalOwner
        fields = (
            'owner_status',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'city',
            'state',
            'zip_code',
            'origin_country',
            'address',
            'comment',
            'profile_image_base',
            'profile_id_image_base',
        )


class AnimalDetailSerializer(AnimalListSerializer):
    health = AnimalHealthSerializer(source='animalhealth', required=False)
    appearance = AnimalAppearanceSerializer(source='animalappearance', required=False)
    training = AnimalTrainingSerializer(source='animaltraining', required=False)
    owners = AnimalOwnerSerializer(source='animalowner_set', many=True, required=False)

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'date_of_birth',
            'age',
            'life_stage',
            'gender',
            'species',
            'breed',
            'species_details',
            'origin_country',
            'pregnant',
            'personality',
            'energy_level',
            'cats_friendly',
            'dogs_friendly',
            'animals_friendly',
            'humans_friendly',
            'kids_friendly',
            'bites',
            'for_adoption',
            'for_foster',
            'accommodation',
            'tag_id',
            'chip_producer',
            'chip_id',
            'joined_reason',
            'entry_date',
            'leave_reason',
            'leave_date',
            'history',
            'image',
            'image_id',
            'adoption_date',
            'fostering_date',
            'sheltering_background',

            'health',
            'appearance',
            'training',
            'owners',
        )

        extra_kwargs = {
            'date_of_birth': {'write_only': True},
        }

    def validate(self, data):
        if data.get('age') and data.get('date_of_birth'):
            raise serializers.ValidationError([_("Set only age or date of birth.")])
        elif (not data.get('age')) and (not data.get('date_of_birth')):
            raise serializers.ValidationError([_("Set either age or date of birth.")])
        return data

    def create(self, validated_data):
        animalhealth = validated_data.pop('animalhealth', {})
        animalhealthcare_set = animalhealth.pop('animalhealthcare_set', [])
        animalappearance = validated_data.pop('animalappearance', {})
        animaltraining = validated_data.pop('animaltraining', {})
        animalowner_set = validated_data.pop('animalowner_set', [])

        animal = Animal.objects.create(**validated_data)

        if animalhealth:
            health = AnimalHealth.objects.create(animal=animal, **animalhealth)
            for animalhealthcare in animalhealthcare_set:
                AnimalHealthCare.objects.create(animal_health=health, **animalhealthcare)

        if animalappearance:
            AnimalAppearance.objects.create(animal=animal, **animalappearance)
        if animaltraining:
            AnimalTraining.objects.create(animal=animal, **animaltraining)
        for animalowner in animalowner_set:
            AnimalOwner.objects.create(animal=animal, **animalowner)
        return animal


class AnimalTableMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalTableMetadata
        fields = (
            'columns',
        )
