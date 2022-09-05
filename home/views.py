import json
from django.shortcuts import render
import requests

# Create your views here.
def base(request):
    city=request.GET.get('city','Gadag')
   
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f4144c3c8583908e0580beb47bfad051'
    data=requests.get(url).json()
    
    payload={ 
        'city':data['name'],
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'kelvin_temperature':data['main']['temp'],
        'celcius_temperature':int(data['main']['temp']-273),
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'description':data['weather'][0]['description'],
        }
    context={
        'data':payload
    }
    return render(request,'home/base.html',context)

