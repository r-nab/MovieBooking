from  django.db import models
from .User import User
from theater.models import ShowTiming, Seat


class Booking(models.Model):
    booked_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    booked_on = models.DateTimeField(auto_now_add=True)
    show_timing = models.ForeignKey(ShowTiming, on_delete=models.SET_NULL, null=True)
    seat = models.ForeignKey(Seat, on_delete=models.SET_NULL, null=True)
