# README for OpenWeatherMap Client and Service

This Python module provides a simple client and service to interact with the OpenWeatherMap API to retrieve current weather and five days forecast data.

## WeatherClient 

The `WeatherClient` class is provides a client for interacting with the OpenWeatherMap API to retrieve weather information.

##  WeatherApiHandler

The `WeatherApiHandler` class is designed to make HTTP requests to the OpenWeatherMap API. It requires an API key for authentication.


## OpenWeatherMapService

The `OpenWeatherMapService` class is a service layer that processes the OpenWeatherMap API responses and extracts relevant weather information. It provides methods to save, retrieve, and clear weather data.


## Example Integration

Here is an example of integrating the `WeatherClient` and `OpenWeatherMapService`:

```python
from owmTestTask.client.weather_client import WeatherClient
from owmTestTask.service.db import DB
from owmTestTask.service.openweathermap_service import OpenWeatherMapService

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = 'your_api_key'
client = WeatherClient(api_key=api_key)
# Example: Get current weather for 'Kharkiv'
weather = client.weather_handler.get_weather_for_city('Kharkiv')
# Example: Save weather data
result_service = OpenWeatherMapService(DB())
result_service.save_weather(weather)
# Example: Get saved weather data
print(result_service.get_weather())

```

Make sure to replace `'your_api_key'` with your actual OpenWeatherMap API key .

Feel free to explore and customize the provided classes based on your application's requirements.

Happy weather data retrieval!