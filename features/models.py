from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    interests = models.CharField(max_length=256)