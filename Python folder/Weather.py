#Weather App using API
import requests
import json

# API key for OpenWeatherMap
api_key = "b14be4bf12b5fc22a6c1bb225a587b4d"

# Base URL for OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Ask the user for the city name
city_name = input("Enter the City name: ")

# Build the URL for the API request
url = base_url + "appid=" + api_key + "&q=" + city_name

# Make the API request
response = requests.get(url)

# Parse the JSON response
data = json.loads(response.text)

# Check if the response contains an error message
if "message" in data:
    print(f"Error: {data['message']}")
else:
    # Print the current weather conditions
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
