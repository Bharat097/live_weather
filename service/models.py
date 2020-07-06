from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    geom = models.PointField()

    def __str__(self):
        return self.name

