from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Location

# Register your models here.
admin.site.register(Location, LeafletGeoAdmin)

