
from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == "POST":
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=a3b45286f60e194dd1ead8c799b3d0c0&units=metric').read()
        temp = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/forecast?q='+city+'&appid=a3b45286f60e194dd1ead8c799b3d0c0&units=metric').read()
        json_data = json.loads(res)
        json_data1 = json.loads(temp)
        data = {
            "timezone": str(json_data['timezone']),
            "temprature":str(json_data['main']['feels_like']),
            "wind":str(json_data['wind']['speed']),
            "humidity":str(json_data['main']['humidity']),
            "weather":str(json_data['weather'][0]['main']),
            "weather_icon": json_data['weather'][0]['icon'],
            "name":str(json_data['name']),
            "time":str(json_data1['list'][7]['dt_txt'])
        }
    else:
        data = {}
    return render(request,'index.html',data)
# Create your views here.
