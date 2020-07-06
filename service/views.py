from django.shortcuts import render, redirect
from .models import Location
from django.http import JsonResponse
import requests
from django.contrib.gis.geos import Point
from django.core.serializers import serialize

# Create your views here.

LAT_LON = "https://api.weather.gov/points/{}"

def index(request):

    if request.method == 'POST':
        try:
            lat = request.POST.get('latitude').strip()
            lon = request.POST.get('longitude').strip()
            name = request.POST.get('name').strip()


            if not (lat and lon and name):
                return JsonResponse({"data": "Invalid Input.."}, status=500)

            location = Location.objects.create(name=name, geom=Point(float(lon), float(lat)))

            location.save()

            return redirect("index")

        except Exception as e:
            # return JsonResponse({"data": str(e)}, status=500)
            raise
    else:

        locations = Location.objects.all()

        locations = serialize('geojson', locations, geometry_field='geom', fields=('name',))

        context = {
            'locations': locations
        }

        return render(request, 'index.html', context)

def fetch_weather(request):
    try:
        lat = request.POST.get('latitude').strip()
        lon = request.POST.get('longitude').strip()
        name = request.POST.get('name').strip()

        param = "{},{}".format(lat, lon)
        url = LAT_LON.format(param)

        # print(url)

        res = requests.get(url)

        if not res.ok:
            res.raise_for_status()

        # # print(res.content)

        grid_url = res.json().get('properties').get('forecast')

        res = requests.get(grid_url)

        if not res.ok:
            res.raise_for_status()

        # return redirect("index")
        # print(res.json())
        p = res.json().get('properties', {}).get('periods', [{}])[0]
        temp = p.get('temperature')
        wind = p.get('windSpeed')
        return JsonResponse({'data': {"temp": temp, "wind": wind, "name": name}}, status=200)

    except Exception as e:
        return JsonResponse({"data": str(e)}, status=500)
        # raise
