from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from .models import ZipCode
import requests
import zipcodes

weather = "BSVlWql7xKgdXKpqB7njSJDT3WHetovS"

@require_POST
def forecast(request):
    base_url = "http://dataservice.accuweather.com/"
    fname = request.POST["fname"]

    try:
        if not zipcodes.is_real(fname):
            return JsonResponse({})
    except ValueError:
        return JsonResponse({})
    if not ZipCode.objects.filter(zip_code=fname).exists():
        response = requests.get(f"{base_url}/locations/v1/postalcodes/search?apikey={weather}&q={fname}")
        if "Code" in response.json():
            #error handle
            return JsonResponse(response.json())
        elif len(response.json()) == 0:
            return JsonResponse({})

        key = response.json()[0]["Key"]
        result_code = response.json()[0]["PrimaryPostalCode"]

        entry = ZipCode.objects.create(zip_code = result_code, location_key = key)
    else:
        object = ZipCode.objects.get(zip_code = fname)
        key = object.location_key

    response = requests.get(f"{base_url}/forecasts/v1/hourly/1hour/{key}?apikey={weather}&details=true")
    return JsonResponse(response.json()[0])