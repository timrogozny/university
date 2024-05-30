import requests



def second():
    url = 'https://randomhistoricalfact.000webhostapp.com/fact'
    response = requests.get(url)
    data = response.json()
    return data['fact']

print("Random historical fact:")
print(second())


def get_weather(city):

    api = 'd66778fc8f5942023f05a2464f428e51'
    url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': api,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'temperature': data['main']['temp'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

city = input("Enter city name: ")
weather = get_weather(city)
if weather:
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Wind Speed: {weather['wind_speed']} m/s")
else:
    print("Error")

