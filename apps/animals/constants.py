from django.utils.translation import gettext_lazy as _


class LifeStages:
    BABY = 'baby'
    YOUNG = 'young'
    ADULT = 'adult'
    SENIOR = 'senior'

    LIFE_STAGES = (
        (BABY, _('Baby')),
        (YOUNG, _('Young')),
        (ADULT, _('Adult')),
        (SENIOR, _('Senior')),
    )


class Genders:
    MALE = 'male'
    FEMALE = 'female'

    GENDERS = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    )


class Species:
    CAT = 'cat'
    DOG = 'dog'
    OTHER = 'other'

    SPECIES = (
        (CAT, _('Cat')),
        (DOG, _('Dog')),
        (OTHER, _('Other')),
    )


class Personalities:
    CALM = 'calm'
    STABLE = 'stable'
    ALERT = 'alert'
    NERVOUS = 'nervous'
    ANXIOUS = 'anxious'
    DEFENSIVE = 'defensive'
    AGGRESSIVE = 'aggressive'

    PERSONALITIES = (
        (CALM, _('Calm')),
        (STABLE, _('Stable')),
        (ALERT, _('Alert')),
        (NERVOUS, _('Nervous')),
        (ANXIOUS, _('Anxious')),
        (DEFENSIVE, _('Defensive')),
        (AGGRESSIVE, _('Aggressive')),
    )


class EnergyLevels:
    LAZY = 'lazy'
    CHILL = 'chill'
    ACTIVE = 'active'
    ENERGETIC = 'energetic'
    HYPER = 'hyper'

    ENERGY_LEVELS = (
        (LAZY, 'Lazy'),
        (CHILL, 'Chill'),
        (ACTIVE, 'Active'),
        (ENERGETIC, 'Energetic'),
        (HYPER, 'Hyper'),
    )


class CatsFriendlyChoices:
    YES = 'yes'
    NO = 'no'
    ONLY_FEMALES = 'only_females'
    ONLY_MALES = 'only_males'

    CATS_FRIENDLY_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONLY_FEMALES, _('Only Females')),
        (ONLY_MALES, _('Only Males')),
    )


class DogsFriendlyChoices:
    YES = 'yes'
    NO = 'no'
    ONLY_FEMALES = 'only_females'
    ONLY_MALES = 'only_males'

    DOGS_FRIENDLY_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONLY_FEMALES, _('Only Females')),
        (ONLY_MALES, _('Only Males')),
    )


class AnimalsFriendlyChoices:
    YES = 'yes'
    NO = 'no'
    ONLY_SMALL_ANIMALS = 'only_small_animals'
    ONLY_BIG_ANIMALS = 'only_big_animals'

    ANIMALS_FRIENDLY_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONLY_SMALL_ANIMALS, _('Only Small Animals')),
        (ONLY_BIG_ANIMALS, _('Only Big Animals')),
    )


class HumansFriendlyChoices:
    YES = 'yes'
    NO = 'no'
    ONLY_FEMALES = 'only_females'
    ONLY_MALES = 'only_males'

    HUMANS_FRIENDLY_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONLY_FEMALES, _('Only Females')),
        (ONLY_MALES, _('Only Males')),
    )


class KidsFriendlyChoices:
    YES = 'yes'
    NO = 'no'
    ONLY_FEMALES = 'only_females'
    ONLY_MALES = 'only_males'
    ONLY_YOUNG_KIDS = 'only_young_kids'
    ONLY_OLD_KIDS = 'only_old_kids'
    BOTH_YOUNG_AND_OLD = 'both_young_and_old'

    KIDS_FRIENDLY_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONLY_FEMALES, _('Only females')),
        (ONLY_MALES, _('Only males')),
        (ONLY_MALES, _('Only young kids')),
        (ONLY_MALES, _('Only old kids')),
        (ONLY_MALES, _('Both young & old')),
    )


class BiteChoices:
    YES = 'yes'
    NO = 'no'

    BITE_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
    )


class AdoptionChoices:
    YES = 'yes'
    NO = 'no'
    HOLD = 'hold'

    ADOPTION_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (HOLD, _('Hold')),
    )


class FosterChoices:
    YES = 'yes'
    NO = 'no'
    HOLD = 'hold'

    FOSTER_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (HOLD, _('Hold')),
    )


class Accommodations:
    APARTMENT = 'apartment'
    HOUSE = 'house'
    VILLA = 'villa'
    FARM = 'farm'
    OTHER = 'other'

    ACCOMMODATIONS = (
        (APARTMENT, _('Apartment')),
        (HOUSE, _('House')),
        (VILLA, _('Villa')),
        (FARM, _('Farm')),
        (OTHER, _('Other')),
    )


class JoinedReasons:
    STRAY = 'stray'
    RESCUE = 'rescue'
    NEGLECTED = 'neglected'
    TRANSFER = 'transfer'
    MEDICAL = 'medical'
    OTHER = 'other'

    JOINED_REASONS = (
        (STRAY, _('Stray')),
        (RESCUE, _('Rescue')),
        (NEGLECTED, _('Neglected')),
        (TRANSFER, _('Transfer')),
        (MEDICAL, _('Medical')),
        (OTHER, _('Other')),
    )


class LeaveReasons:
    ADOPTION = 'adoption'
    FOSTER = 'foster'
    MEDICAL = 'medical'
    TEMPORARY = 'temporary'
    DEATH = 'death'
    OTHER = 'other'

    LEAVE_REASONS = (
        (ADOPTION, _('Adoption')),
        (FOSTER, _('Foster')),
        (MEDICAL, _('Medical')),
        (TEMPORARY, _('Temporary')),
        (DEATH, _('Death')),
        (OTHER, _('Other')),
    )


class WeightConditions:
    NORMAL = 'normal'
    UNDERWEIGHT = 'underweight'
    OVERWEIGHT = 'overweight'

    WEIGHT_CONDITIONS = (
        (NORMAL, _('Normal')),
        (UNDERWEIGHT, _('Underweight')),
        (OVERWEIGHT, _('Overweight')),
    )


class SterilizedChoices:
    SPAYED = 'spayed'
    NEUTERED = 'neutered'

    STERILIZED = (
        (SPAYED, _('Spayed')),
        (NEUTERED, _('Neutered')),
    )


class EyesSights:
    CLEAR = 'clear'
    DISCHARGE = 'discharge'
    CLOUDY = 'cloudy'
    INJURED = 'injured'

    EYES_SIGHTS = (
        (CLEAR, _('Clear')),
        (DISCHARGE, _('Discharge')),
        (CLOUDY, _('Cloudy')),
        (INJURED, _('Injured')),
    )


class BlindChoices:
    YES = 'yes'
    NO = 'no'
    ONE_EYE = 'one_eye'

    BLIND_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONE_EYE, _('One eye')),
    )


class DeafChoices:
    YES = 'yes'
    NO = 'no'
    ONE_EAR = 'one_ear'

    DEAF_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONE_EAR, _('One ear')),
    )


class TeethChoices:
    CLEAN = 'clean'
    TARTAR = 'tartar'
    ROTTEN = 'rotten'
    ABSCESS_OR_SORES = 'abscess_or_sores'
    WORN = 'worn'
    IMPACTED = 'impacted'
    FEW_MISSING = 'few_missing'
    NONE = 'none'

    TEETH_CHOICES = (
        (CLEAN, _('clean')),
        (TARTAR, _('tartar')),
        (ROTTEN, _('rotten')),
        (ABSCESS_OR_SORES, _('Abscess/Sores')),
        (WORN, _('Worn')),
        (IMPACTED, _('Impacted')),
        (FEW_MISSING, _('Few missing')),
        (NONE, _('None')),
    )


class Gums:
    PINK = 'pink'
    RED = 'red'
    WHITE = 'white'
    ABSCESS_OR_SORES = 'abscess_or_sores'

    GUMS = (
        (PINK, _('Pink')),
        (RED, _('Red')),
        (WHITE, _('White')),
        (ABSCESS_OR_SORES, _('Abscess/Sores')),
    )


class Sizes:
    EXTRA_SMALL = 'extra_small'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    EXTRA_LARGE = 'extra_large'

    SIZES = (
        (EXTRA_SMALL, _('Extra small')),
        (SMALL, _('Small')),
        (MEDIUM, _('Medium')),
        (LARGE, _('Large')),
        (EXTRA_LARGE, _('Extra large')),
    )


class CoatColors:
    BLACK = 'Black'
    GREY = 'Grey'
    WHITE = 'White'
    BROWN = 'Brown'
    RED = 'Red'
    ORANGE = 'Orange'
    YELLOW = 'Yellow'
    CREAM = 'Cream'
    FAWN = 'Fawn'

    COAT_COLORS = (
        (BLACK, _('Black')),
        (GREY, _('Grey')),
        (WHITE, _('White')),
        (BROWN, _('Brown')),
        (RED, _('Red ')),
        (ORANGE, _('Orange')),
        (YELLOW, _('Yellow')),
        (CREAM, _('Cream')),
        (FAWN, _('Fawn')),
    )


class CoatMarks:
    STRIPPED = 'stripped'
    DOTTED = 'dotted'

    COAT_MARKS = (
        (STRIPPED, _('Stripped')),
        (DOTTED, _('Dotted')),
    )


class EyeColors:
    BLACK = 'black'
    GREY = 'grey'
    BROWN = 'brown'
    HAZEL = 'hazel'
    GREEN = 'green'
    BLUE = 'blue'

    EYE_COLORS = (
        (BLACK, _('Black')),
        (GREY, _('Grey')),
        (BROWN, _('Brown')),
        (HAZEL, _('Hazel')),
        (GREEN, _('Green')),
        (BLUE, _('Blue')),
    )


class EarChoices:
    POINTING = 'pointing'
    CROPPED = 'cropped'
    FLAPPING = 'flapping'
    ROUND = 'round'

    EAR_CHOICES = (
        (POINTING, _('Pointing')),
        (CROPPED, _('Cropped')),
        (FLAPPING, _('Flapping')),
        (ROUND, _('Round')),
    )


class TailChoices:
    SHORT = 'short'
    LONG = 'long'
    DOCKED = 'docked'

    TAIL_CHOICES = (
        (SHORT, _('Short')),
        (LONG, _('Long')),
        (DOCKED, _('Docked')),
    )


class ObedienceChoices:
    NONE = 'none'
    BASIC = 'basic'
    ADVANCED = 'advanced'
    PROFESSIONAL = 'professional'

    OBEDIENCE_CHOICES = (
        (NONE, _('None')),
        (BASIC, _('Basic')),
        (ADVANCED, _('Advanced')),
        (PROFESSIONAL, _('Professional')),
    )


class OwnerChoices:
    EXISTING_OWNER = 'existing_owner'
    PREVIOUS_OWNER = 'previous_owner'
    FOSTER = 'foster'
    ADOPTER = 'adopter'
    NO_OWNER = 'no_owner'

    OWNER_CHOICES = (
        (EXISTING_OWNER, _('Existing Owner')),
        (PREVIOUS_OWNER, _('Previous Owner')),
        (FOSTER, _('Foster')),
        (ADOPTER, _('Adopter')),
        (NO_OWNER, _('No Owner')),
    )
