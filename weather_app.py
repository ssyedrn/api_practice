# Program: Weather App
# Description: Fetches current weather for a city using the OpenWeatherMap API.
# Covers: API calls, JSON parsing, environment variables, exception handling, user input.

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print(f"Error: {data.get('message', 'City not found')}")
            return

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except KeyError:
        print("Unexpected response format from API.")

def main():
    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            print("Goodbye!")
            break
        if not city:
            print("City name cannot be empty.")
            continue
        get_weather(city)

if __name__ == "__main__":
    main()
