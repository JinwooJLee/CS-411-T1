from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

# Create your views here.
def index(request):
    json = [{"DateTime":"2021-11-13T18:00:00-05:00","EpochDateTime":1636844400,"WeatherIcon":15,"IconPhrase":"Thunderstorms","HasPrecipitation":True,"PrecipitationType":"Rain","PrecipitationIntensity":"Moderate","IsDaylight":False,"Temperature":{"Value":51.0,"Unit":"F","UnitType":18},"PrecipitationProbability":51,"MobileLink":"http://www.accuweather.com/en/us/boston-ma/02108/hourly-weather-forecast/348735?day=1&hbhhour=18&lang=en-us","Link":"http://www.accuweather.com/en/us/boston-ma/02108/hourly-weather-forecast/348735?day=1&hbhhour=18&lang=en-us"}]
    return JsonResponse(json[0])