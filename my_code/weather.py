# смотрим погоду http://openweathermap.org/current
# идея https://habrahabr.ru/post/315264/
# http://api.openweathermap.org/data/2.5/weather?&id=524901&APPID=ca8e56cb187383c6834b7cab8a8743e3&units=metric&&lang=ru

import requests

appid = 'ca8e56cb187383c6834b7cab8a8743e3'
url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&&lang=ru'
cities = ['524901', # Moscow
          '480562' #Tula
          ]

def generate_url(city_id):
    global appid
    global url
    return url + '&id=' + city_id +  '&APPID=' + appid

try:
    result = requests.get(generate_url(cities[0]))
    data = result.json()
    print(data['main']['temp']) # температура
    print(data['main']['pressure']) #
    print(data['main']['humidity'])#
    print(data['visibility'])# видимость
    print(data['wind']['speed']) # скорость ветра
    print(data['description']) # скорость ветра


except Exception as e:
    print("Exception (find):", e)
    pass