from django.db import models

class Placemark(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    latitude = models.FloatField()
    longitude = models.FloatField()
