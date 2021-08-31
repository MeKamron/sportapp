from django.db import models
from location_field.models.plain import PlainLocationField


class SportTuri(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class SportCenter(models.Model):
    nomi = models.CharField(max_length=255)
    sport_turi = models.ForeignKey(SportTuri, on_delete=models.SET_NULL, null=True, blank=True, related_name="sport_centers")
    manzil = models.CharField(max_length=255)
    telfon = models.CharField(max_length=25)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longtitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.nomi