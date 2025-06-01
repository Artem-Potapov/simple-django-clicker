import django

from django.db import models

# Create your models here.

class Clicks(models.Model):
    count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
