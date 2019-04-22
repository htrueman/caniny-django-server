import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .constants import UserTypes


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, id, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        user = self.model(id=id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, id=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(id, password, **extra_fields)

    def create_superuser(self, id, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        null=True
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150,
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
        null=True,
        unique=True
    )
    address = models.CharField(
        _('address'),
        max_length=256,
        null=True,
        blank=True
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
    description = models.TextField(
        blank=True,
        null=True
    )
    profile_image = models.ImageField(
        upload_to='users/profile_images',
        null=True,
        blank=True
    )

    # social identifiers
    google_key = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        unique=True
    )
    instagram_key = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        unique=True
    )
    facebook_key = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        unique=True
    )

    organization = models.ForeignKey(
        'organizations.Organization',
        on_delete=models.CASCADE,
        null=True
    )

    user_type = models.CharField(
        choices=UserTypes.USER_TYPES,
        default=UserTypes.HELPER,
        max_length=12
    )

    USERNAME_FIELD = 'id'
    AUTH_FIELDS = (
        'email',
        'google_key',
        'instagram_key',
        'facebook_key',
    )

    objects = UserManager()

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.is_staff and self.is_superuser:
            self.user_type = UserTypes.DJANGO_ADMIN

        super().save(*args, **kwargs)
