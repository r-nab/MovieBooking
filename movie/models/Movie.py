from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    length_mins = models.PositiveIntegerField()

    class Meta:
        unique_together = ["name", "year"]

