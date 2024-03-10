from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    contact_number = models.CharField(max_length=11)
    town = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name

