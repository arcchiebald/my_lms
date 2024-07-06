from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class LmsUser(AbstractUser):
    phone = models.IntegerField(blank=True, null=True)
    
    