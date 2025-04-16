import requests

API_KEY = 'your_api_key_here'  # 🔐 Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # or 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print_weather(data)
    else:
        print("❌ Error: City not found or API issue.")

def print_weather(data):
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels = data['main']['feels_like']
    weather = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']

    print(f"\n📍 Weather in {city}, {country}")
    print(f"🌡️ Temp: {temp}°C (Feels like: {feels}°C)")
    print(f"🌥️ Condition: {weather.capitalize()}")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️ Wind Speed: {wind} m/s\n")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
