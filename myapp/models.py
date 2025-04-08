from django.contrib.auth.models import AbstractUser
from django.db import models




# Custom User model with additional fields
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    pass
