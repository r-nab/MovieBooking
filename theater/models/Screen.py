from django.db import models
from .Theater import Theater


class Screen(models.Model):
    screen_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=False)
    theater = models.ManyToManyField(Theater, through='ScreenTheater')



class ScreenTheater(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
