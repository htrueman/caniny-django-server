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
    UNKNOWN = 'unknown'

    CATS_FRIENDLY_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONLY_FEMALES, _('Only Females')),
        (ONLY_MALES, _('Only Males')),
        (UNKNOWN, _('Unknown')),
    )


class DogsFriendlyChoices:
    YES = 'yes'
    NO = 'no'
    ONLY_FEMALES = 'only_females'
    ONLY_MALES = 'only_males'
    UNKNOWN = 'unknown'

    DOGS_FRIENDLY_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONLY_FEMALES, _('Only Females')),
        (ONLY_MALES, _('Only Males')),
        (UNKNOWN, _('Unknown')),
    )


class AnimalsFriendlyChoices:
    YES = 'yes'
    NO = 'no'
    ONLY_SMALL_ANIMALS = 'only_small_animals'
    ONLY_BIG_ANIMALS = 'only_big_animals'
    UNKNOWN = 'unknown'

    ANIMALS_FRIENDLY_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONLY_SMALL_ANIMALS, _('Only Small Animals')),
        (ONLY_BIG_ANIMALS, _('Only Big Animals')),
        (UNKNOWN, _('Unknown')),
    )


class HumansFriendlyChoices:
    YES = 'yes'
    NO = 'no'
    ONLY_FEMALES = 'only_females'
    ONLY_MALES = 'only_males'
    UNKNOWN = 'unknown'

    HUMANS_FRIENDLY_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONLY_FEMALES, _('Only Females')),
        (ONLY_MALES, _('Only Males')),
        (UNKNOWN, _('Unknown')),
    )


class KidsFriendlyChoices:
    YES = 'yes'
    NO = 'no'
    ONLY_FEMALES = 'only_females'
    ONLY_MALES = 'only_males'
    ONLY_YOUNG_KIDS = 'only_young_kids'
    ONLY_OLD_KIDS = 'only_old_kids'
    BOTH_YOUNG_AND_OLD = 'both_young_and_old'
    UNKNOWN = 'unknown'

    KIDS_FRIENDLY_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ONLY_FEMALES, _('Only females')),
        (ONLY_MALES, _('Only males')),
        (ONLY_YOUNG_KIDS, _('Only young kids')),
        (ONLY_OLD_KIDS, _('Only old kids')),
        (BOTH_YOUNG_AND_OLD, _('Both young & old')),
        (UNKNOWN, _('Unknown')),
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
    TO_BE = 'to_be'
    HOLD = 'hold'

    ADOPTION_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (TO_BE, _('To be')),
        (HOLD, _('Hold')),
    )


class FosterChoices:
    YES = 'yes'
    NO = 'no'
    TO_BE = 'to_be'
    HOLD = 'hold'

    FOSTER_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No')),
        (TO_BE, _('To be')),
        (HOLD, _('Hold')),
    )


class Accommodations:
    APARTMENT = 'apartment'
    TOWNHOUSE = 'townhouse'
    HOUSE = 'house'
    VILLA = 'villa'
    FARM = 'farm'
    OTHER = 'other'

    ACCOMMODATIONS = (
        (APARTMENT, _('Apartment')),
        (TOWNHOUSE, _('Townhouse')),
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
    TEMPORARY = 'temporary'
    OTHER = 'other'

    JOINED_REASONS = (
        (STRAY, _('Stray')),
        (RESCUE, _('Rescue')),
        (NEGLECTED, _('Neglected')),
        (TRANSFER, _('Transfer')),
        (MEDICAL, _('Medical')),
        (TEMPORARY, _('Temporary')),
        (OTHER, _('Other')),
    )


class LeaveReasons:
    ADOPTION = 'adoption'
    FOSTER = 'foster'
    MEDICAL = 'medical'
    TEMPORARY = 'temporary'
    DEATH = 'death'
    TRANSFER = 'transfer'
    OTHER = 'other'

    LEAVE_REASONS = (
        (ADOPTION, _('Adoption')),
        (FOSTER, _('Foster')),
        (MEDICAL, _('Medical')),
        (TEMPORARY, _('Temporary')),
        (DEATH, _('Death')),
        (TRANSFER, _('Transfer')),
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


class CoatTypes:
    SHORT = 'short'
    MEDIUM = 'medium'
    LONG = 'long'
    HAIRLESS = 'hairless'

    COAT_TYPES = (
        (SHORT, _('Short')),
        (MEDIUM, _('Medium')),
        (LONG, _('Long')),
        (HAIRLESS, _('Hairless')),
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
    OTHER = 'other'

    OWNER_CHOICES = (
        (EXISTING_OWNER, _('Existing Owner')),
        (PREVIOUS_OWNER, _('Previous Owner')),
        (FOSTER, _('Foster')),
        (ADOPTER, _('Adopter')),
        (NO_OWNER, _('No Owner')),
        (OTHER, _('Other')),
    )


class CareTypes:
    VACCINATION = 'vaccination'
    MEDICINE = 'medicine'
    GROOMING = 'grooming'
    BOARDING = 'boarding'
    OTHER = 'other'

    CARE_TYPES = (
        (VACCINATION, _('Vaccination')),
        (MEDICINE, _('Medicine')),
        (GROOMING, _('Grooming')),
        (BOARDING, _('Boarding')),
        (OTHER, _('Other')),
    )


COUNTRIES = [
    ('US', 'United States'),
    ('AF', 'Afghanistan'),
    ('AL', 'Albania'),
    ('DZ', 'Algeria'),
    ('AS', 'American Samoa'),
    ('AD', 'Andorra'),
    ('AO', 'Angola'),
    ('AI', 'Anguilla'),
    ('AQ', 'Antarctica'),
    ('AG', 'Antigua And Barbuda'),
    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AW', 'Aruba'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'),
    ('BH', 'Bahrain'),
    ('BD', 'Bangladesh'),
    ('BB', 'Barbados'),
    ('BY', 'Belarus'),
    ('BE', 'Belgium'),
    ('BZ', 'Belize'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BT', 'Bhutan'),
    ('BO', 'Bolivia'),
    ('BA', 'Bosnia And Herzegowina'),
    ('BW', 'Botswana'),
    ('BV', 'Bouvet Island'),
    ('BR', 'Brazil'),
    ('BN', 'Brunei Darussalam'),
    ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('KH', 'Cambodia'),
    ('CM', 'Cameroon'),
    ('CA', 'Canada'),
    ('CV', 'Cape Verde'),
    ('KY', 'Cayman Islands'),
    ('CF', 'Central African Rep'),
    ('TD', 'Chad'),
    ('CL', 'Chile'),
    ('CN', 'China'),
    ('CX', 'Christmas Island'),
    ('CC', 'Cocos Islands'),
    ('CO', 'Colombia'),
    ('KM', 'Comoros'),
    ('CG', 'Congo'),
    ('CK', 'Cook Islands'),
    ('CR', 'Costa Rica'),
    ('CI', 'Cote D`ivoire'),
    ('HR', 'Croatia'),
    ('CU', 'Cuba'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DK', 'Denmark'),
    ('DJ', 'Djibouti'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('TP', 'East Timor'),
    ('EC', 'Ecuador'),
    ('EG', 'Egypt'),
    ('SV', 'El Salvador'),
    ('GQ', 'Equatorial Guinea'),
    ('ER', 'Eritrea'),
    ('EE', 'Estonia'),
    ('ET', 'Ethiopia'),
    ('FK', 'Falkland Islands (Malvinas)'),
    ('FO', 'Faroe Islands'),
    ('FJ', 'Fiji'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('GF', 'French Guiana'),
    ('PF', 'French Polynesia'),
    ('TF', 'French S. Territories'),
    ('GA', 'Gabon'),
    ('GM', 'Gambia'),
    ('GE', 'Georgia'),
    ('DE', 'Germany'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GR', 'Greece'),
    ('GL', 'Greenland'),
    ('GD', 'Grenada'),
    ('GP', 'Guadeloupe'),
    ('GU', 'Guam'),
    ('GT', 'Guatemala'),
    ('GN', 'Guinea'),
    ('GW', 'Guinea-bissau'),
    ('GY', 'Guyana'),
    ('HT', 'Haiti'),
    ('HN', 'Honduras'),
    ('HK', 'Hong Kong'),
    ('HU', 'Hungary'),
    ('IS', 'Iceland'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),
    ('IR', 'Iran'),
    ('IQ', 'Iraq'),
    ('IE', 'Ireland'),
    ('IL', 'Israel'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JP', 'Japan'),
    ('JO', 'Jordan'),
    ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'),
    ('KI', 'Kiribati'),
    ('KP', 'Korea (North)'),
    ('KR', 'Korea (South)'),
    ('KW', 'Kuwait'),
    ('KG', 'Kyrgyzstan'),
    ('LA', 'Laos'),
    ('LV', 'Latvia'),
    ('LB', 'Lebanon'),
    ('LS', 'Lesotho'),
    ('LR', 'Liberia'),
    ('LY', 'Libya'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('MO', 'Macau'),
    ('MK', 'Macedonia'),
    ('MG', 'Madagascar'),
    ('MW', 'Malawi'),
    ('MY', 'Malaysia'),
    ('MV', 'Maldives'),
    ('ML', 'Mali'),
    ('MT', 'Malta'),
    ('MH', 'Marshall Islands'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauritania'),
    ('MU', 'Mauritius'),
    ('YT', 'Mayotte'),
    ('MX', 'Mexico'),
    ('FM', 'Micronesia'),
    ('MD', 'Moldova'),
    ('MC', 'Monaco'),
    ('MN', 'Mongolia'),
    ('MS', 'Montserrat'),
    ('MA', 'Morocco'),
    ('MZ', 'Mozambique'),
    ('MM', 'Myanmar'),
    ('NA', 'Namibia'),
    ('NR', 'Nauru'),
    ('NP', 'Nepal'),
    ('NL', 'Netherlands'),
    ('AN', 'Netherlands Antilles'),
    ('NC', 'New Caledonia'),
    ('NZ', 'New Zealand'),
    ('NI', 'Nicaragua'),
    ('NE', 'Niger'),
    ('NG', 'Nigeria'),
    ('NU', 'Niue'),
    ('NF', 'Norfolk Island'),
    ('MP', 'Northern Mariana Islands'),
    ('NO', 'Norway'),
    ('OM', 'Oman'),
    ('PK', 'Pakistan'),
    ('PW', 'Palau'),
    ('PA', 'Panama'),
    ('PG', 'Papua New Guinea'),
    ('PY', 'Paraguay'),
    ('PE', 'Peru'),
    ('PH', 'Philippines'),
    ('PN', 'Pitcairn'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('PR', 'Puerto Rico'),
    ('QA', 'Qatar'),
    ('RE', 'Reunion'),
    ('RO', 'Romania'),
    ('RU', 'Russian Federation'),
    ('RW', 'Rwanda'),
    ('KN', 'Saint Kitts And Nevis'),
    ('LC', 'Saint Lucia'),
    ('VC', 'St Vincent/Grenadines'),
    ('WS', 'Samoa'),
    ('SM', 'San Marino'),
    ('ST', 'Sao Tome'),
    ('SA', 'Saudi Arabia'),
    ('SN', 'Senegal'),
    ('SC', 'Seychelles'),
    ('SL', 'Sierra Leone'),
    ('SG', 'Singapore'),
    ('SK', 'Slovakia'),
    ('SI', 'Slovenia'),
    ('SB', 'Solomon Islands'),
    ('SO', 'Somalia'),
    ('ZA', 'South Africa'),
    ('ES', 'Spain'),
    ('LK', 'Sri Lanka'),
    ('SH', 'St. Helena'),
    ('PM', 'St.Pierre'),
    ('SD', 'Sudan'),
    ('SR', 'Suriname'),
    ('SZ', 'Swaziland'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('SY', 'Syrian Arab Republic'),
    ('TW', 'Taiwan'),
    ('TJ', 'Tajikistan'),
    ('TZ', 'Tanzania'),
    ('TH', 'Thailand'),
    ('TG', 'Togo'),
    ('TK', 'Tokelau'),
    ('TO', 'Tonga'),
    ('TT', 'Trinidad And Tobago'),
    ('TN', 'Tunisia'),
    ('TR', 'Turkey'),
    ('TM', 'Turkmenistan'),
    ('TV', 'Tuvalu'),
    ('UG', 'Uganda'),
    ('UA', 'Ukraine'),
    ('AE', 'United Arab Emirates'),
    ('UK', 'United Kingdom'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VU', 'Vanuatu'),
    ('VA', 'Vatican City State'),
    ('VE', 'Venezuela'),
    ('VN', 'Viet Nam'),
    ('VG', 'Virgin Islands (British)'),
    ('VI', 'Virgin Islands (U.S.)'),
    ('EH', 'Western Sahara'),
    ('YE', 'Yemen'),
    ('YU', 'Yugoslavia'),
    ('ZR', 'Zaire'),
    ('ZM', 'Zambia'),
    ('ZW', 'Zimbabwe')
]
