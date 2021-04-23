from django.db import models
from .Screen import Screen

class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    screen = models.ManyToManyField(Screen)
    is_premium = models.BooleanField(default=False)
