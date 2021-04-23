from django.db import models
from movie.models import Movie
from .Screen import ScreenTheater


class ShowTiming(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True, related_name='show_movie')
    screen_theater = models.ForeignKey(ScreenTheater, on_delete=models.SET_NULL, null=True)
