from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
import requests

weather = "BSVlWql7xKgdXKpqB7njSJDT3WHetovS"

@require_POST
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