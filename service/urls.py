from django.contrib import admin
from django.urls import path, include
from djgeojson.views import GeoJSONLayerView
from . import views
from .models import Location

urlpatterns = [
    path('', views.index, name="index"),
    path('fetch_weather', views.fetch_weather, name="fetch_weather"),
    path('data', GeoJSONLayerView.as_view(model=Location, properties=('name')), name="geojson")
]