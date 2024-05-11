from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import UserManager


class CustomUser(AbstractUser):
    contact_number = models.CharField(max_length=11, unique=True)
    email = None
    username = models.CharField(max_length=10, null=True, blank=True, unique=False)

    USERNAME_FIELD = 'contact_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name
