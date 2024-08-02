import requests

API_KEY = 'API_KEY'
air = 'null'

def get_weather_data(city):
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: HTTP {response.status_code}")
        print(f"Response: {response.text}")
        return None

def display_weather_info(weather_data, city):
    if weather_data:
        main = weather_data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather = weather_data['weather'][0]['description']

        if temperature > 30:
            air = "it's very hot"
        elif 15 <= temperature <= 30:
            air = "it's warm"
        elif 0 <= temperature <=14:
            air = "it's cold"
        else:
            air = "its like ice"

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C and "+ air)
        print(f"Condition: {weather}")
        print(f"Humidity: {humidity}%")

    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    city = input("Enter a city for the weather information: ")
    weather_data = get_weather_data(city)
    display_weather_info(weather_data, city)
