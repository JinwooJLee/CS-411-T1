from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from .models import ZipCode
import requests
import zipcodes

weather = "BSVlWql7xKgdXKpqB7njSJDT3WHetovS"

@require_POST
def forecast(request):
    base_url = "http://dataservice.accuweather.com/" #Base url for api
    fname = request.POST["fname"] #Zipcode entry in the form

    #Check to see if the zipcode if valid
    try:
        if not zipcodes.is_real(fname):
            return JsonResponse({}) #Return emtpy response if it is not
    except ValueError: #Occurs if the input string contains more than just numbers and hyphen
        return JsonResponse({})

    #After validating Zipcode
    if not ZipCode.objects.filter(zip_code=fname).exists(): #Check to see if zip code and location key is already in database
        #Query AccuWeather API  for zip code's location key
        response = requests.get(f"{base_url}/locations/v1/postalcodes/search?apikey={weather}&q={fname}")
        if "Code" in response.json():
            #error handle
            return JsonResponse(response.json())
        elif len(response.json()) == 0:
            #empty response
            return JsonResponse({})

        #create new entry in the database with the zipcode and location key
        key = response.json()[0]["Key"]
        result_code = response.json()[0]["PrimaryPostalCode"]
        entry = ZipCode.objects.create(zip_code = result_code, location_key = key)

    else: #zipcode already exists within database, get location key from there
        object = ZipCode.objects.get(zip_code = fname)
        key = object.location_key

    #Query AccuWeather API for 1 hour forecast of given zipcode and return the first result.
    response = requests.get(f"{base_url}/forecasts/v1/hourly/1hour/{key}?apikey={weather}&details=true")
    return JsonResponse(response.json()[0])