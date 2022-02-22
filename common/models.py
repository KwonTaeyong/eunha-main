from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100,null=True)
    rank = models.CharField(max_length=100,null=True)


# Create your models here.
