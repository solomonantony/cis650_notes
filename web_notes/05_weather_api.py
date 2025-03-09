""" There are many web services that serve json data when requested via an API call.
Almost all web services require the consumer to get her/his own private API key.
That API key must be submitted every time a request is sent.
For getting current weather data, https://openweathermap.org/api is one such web service.
At this site there are many API's available.
There is one API for getting weather by city name, another API for getting weather by ZIP code, and another one for weather by geo coordinates and so on.
Shown below is an example Python script that accesses the ZIP based API for current weather.
"""
import urllib.request, urllib.parse, urllib.error
import json

# Note get yourself a free account at openweathermap.org 
Sign up at https://openweathermap.org/api
# find your api key use it in place appid

serviceurl = 'https://api.openweathermap.org/data/2.5/weather?'
#get your api key at https://openweathermap.org/faq#error401
appid = "xxx"
while True:
    zip = input('Enter ZIP code: ')
    if len(zip) < 1: break

    url = serviceurl + "zip=" + zip +"&appid=" + appid


    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
        print(json.dumps(js, indent=4)) #formatted for human eyes
    except:
        js = None
