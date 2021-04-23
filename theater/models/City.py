from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    area = models.TextField()
    area_pin = models.PositiveIntegerField()
