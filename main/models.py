from django.db import models


class SportTuri(models.Model):
    nomi = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="sport_turlar/", blank=True)

    def __str__(self):
        return self.nomi


class SportCenter(models.Model):
    nomi = models.CharField(max_length=255)
    sport_turi = models.ForeignKey(SportTuri, on_delete=models.SET_NULL, null=True, blank=True, related_name="sport_centers")
    manzil = models.CharField(max_length=255)
    telfon = models.CharField(max_length=25)
    opens = models.TimeField()
    closes = models.TimeField()
    photo = models.ImageField(upload_to="sport_centers/", blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longtitude = models.DecimalField(max_digits=9, decimal_places=6)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nomi

    
    class Meta:
        ordering = ('nomi',)
        