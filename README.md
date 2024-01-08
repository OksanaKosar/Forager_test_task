# README for OpenWeatherMap Client and Service

This Python module provides a simple client and service to interact with the OpenWeatherMap API to retrieve current weather and five days forecast data.

## OpenWeatherMapClient 

The `OpenWeatherMapClient` class is provides a client for interacting with the OpenWeatherMap API to retrieve weather information.

##  WeatherApiHandler

The `WeatherApiHandler` class is designed to make HTTP requests to the OpenWeatherMap API. It requires an API key for authentication.


## OpenWeatherMapService

The `OpenWeatherMapService` class is a service layer that processes the OpenWeatherMap API responses and extracts relevant weather information. It provides methods to save, retrieve, and clear weather data.


## Example Integration

Here is an example of integrating the `OpenWeatherMapClient` and `OpenWeatherMapService`:

```python
from owmTestTask.client.client import Client
from owmTestTask.service.openweathermap_service import OpenWeatherMapService
from owmTestTask.client.weather_api import WeatherApiHandler
from owmTestTask.client.request_type_enums import RequestType
from owmTestTask.service.db import DB

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = 'your_api_key'
weather_handler = WeatherApiHandler(api_key)
client = Client(weather_handler)

# Example: Get current weather
forecast = client.weather(request_type=RequestType.current, lat='48.92', lon='24.71')

# Example: Save weather data
result_service = OpenWeatherMapService(DB())
result_service.save_weather(forecast)

# Example: Get saved weather data
print(result_service.get_weather())
```

Make sure to replace `'your_api_key'`, `latitude`, and `longitude` with your actual OpenWeatherMap API key and geographical coordinates.

Feel free to explore and customize the provided classes based on your application's requirements.

Happy weather data retrieval!