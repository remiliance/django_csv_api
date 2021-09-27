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
