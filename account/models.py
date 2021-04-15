from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

Choice_Reg = (
    ('Doctor', 'Doctor'),
    ('patient', 'patient'),

)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    a user profile in our system
    """
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    Choice = models.CharField(max_length=25, choices=Choice_Reg)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = BaseUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'Choice']

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        """
        What to show when we output an object as a string
        """

        return self.name
