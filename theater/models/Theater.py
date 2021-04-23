from django.db import models
from .City import City


class Theater(models.Model):
    name = models.CharField(max_length=200, unique=True)
    cities = models.ManyToManyField(City)
