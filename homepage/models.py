from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
