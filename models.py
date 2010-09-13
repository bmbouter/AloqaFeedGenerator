from django.db import models

class Placemark(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    latitude = models.FloatField()
    longitude = models.FloatField()
    url = URLField(blank=True, verify_exists=True)
    phone_number = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    show_map = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s Placemark" % self.name
