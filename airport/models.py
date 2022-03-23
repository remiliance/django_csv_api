from time import strftime

from django.db import models
from airport.enum import MOVE, FLIGHTTYPE


class Traffic(models.Model):
    DATA_EXTRACT_DATE = models.DateTimeField()
    REPORT_PERIOD = models.DateTimeField()
    TERMINAL = models.CharField(max_length=100)
    ARRIVAL_DEPARTURE = models.CharField(max_length=20, choices=MOVE)
    DOMESTIC_INTERNATIONAL = models.CharField(max_length=20, choices=FLIGHTTYPE)
    PASSENGER_COUNT = models.IntegerField()

    def __str__(self):
        t=self.DATA_EXTRACT_DATE
        return t.strftime('%m/%d/%Y') + self.ARRIVAL_DEPARTURE  # donne '02/23/2012'


class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)

class Album(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)


class BookingLines(models.Model):
    album = models.OneToOneField(Album, on_delete=models.DO_NOTHING)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)