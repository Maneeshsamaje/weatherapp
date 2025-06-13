from django.shortcuts import render
import requests

# Create your views here.

def index(request):

    city = request.GET.get('city')

    api_key = "18fd8cd7758ab972d149faa2edf3e6cd"

    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    print(api_url)

    api = requests.get(api_url).json()

    temperature = api['main']['temp']

    city = api['name']

    country = api['sys']['country']

    return render(request,'index.html',{'temperature':temperature, 'city':city, 'country':country})

