from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        null=True
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150,
        blank=True,
        null=True
    )
    phone_number = PhoneNumberField(
        _('phone number'),
        null=True,
        blank=True,
        unique=True
    )
    email = models.EmailField(
        _('email address'),
        blank=True,
        null=True,
        unique=True
    )
    address = models.CharField(
        _('email address'),
        max_length=256
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    # social identifiers
    google_key = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    instagram_key = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    facebook_key = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'email'
