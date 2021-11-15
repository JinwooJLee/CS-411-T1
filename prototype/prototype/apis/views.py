from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
import requests

weather = "BSVlWql7xKgdXKpqB7njSJDT3WHetovS"

# Create your views here.
def index(request):
    json = [{'test': 'hello', "DateTime":"2021-11-13T18:00:00-05:00","EpochDateTime":1636844400,"WeatherIcon":15,"IconPhrase":"Thunderstorms","HasPrecipitation":True,"PrecipitationType":"Rain","PrecipitationIntensity":"Moderate","IsDaylight":False,"Temperature":{"Value":51.0,"Unit":"F","UnitType":18},"PrecipitationProbability":51,"MobileLink":"http://www.accuweather.com/en/us/boston-ma/02108/hourly-weather-forecast/348735?day=1&hbhhour=18&lang=en-us","Link":"http://www.accuweather.com/en/us/boston-ma/02108/hourly-weather-forecast/348735?day=1&hbhhour=18&lang=en-us"}]
    return JsonResponse(json[0])

def forecast(request):
    base_url = "http://dataservice.accuweather.com/"
    zipcode = request.POST["fname"]
    
    response = requests.get(f"{base_url}/locations/v1/postalcodes/search?apikey={weather}&q={zipcode}")
    if "Code" in response.json():
        #error handle
        return JsonResponse(response.json())
    elif len(response.json()) == 0:
        return JsonResponse({})

    key = response.json()[0]["Key"]

    response = requests.get(f"{base_url}/forecasts/v1/hourly/1hour/{key}?apikey={weather}&details=true")
    return JsonResponse(response.json()[0])