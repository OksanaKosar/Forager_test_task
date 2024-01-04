# README for OpenWeatherMap Client and Service

This Python module provides a simple client and service to interact with the OpenWeatherMap API to retrieve current weather and five days forecast data.

## OpenWeatherMapClient

The `OpenWeatherMapClient` class is designed to make HTTP requests to the OpenWeatherMap API. It requires an API key for authentication.


## OpenWeatherMapService

The `OpenWeatherMapService` class is a service layer that processes the OpenWeatherMap API responses and extracts relevant weather information. It provides methods to save, retrieve, and clear weather data.


## Example Integration

Here is an example of integrating the `OpenWeatherMapClient` and `OpenWeatherMapService`:

```python
from open_weather_map_client import OpenWeatherMapClient
from open_weather_map_service import OpenWeatherMapService

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = 'your_api_key'
weather_client = OpenWeatherMapClient(api_key)
weather_service = OpenWeatherMapService()

# Example: Get current weather
current_weather = weather_client.get_current_weather(latitude, longitude)

# Example: Save weather data
weather_service.save_weather(current_weather)

# Example: Get saved weather data
saved_weather_data = weather_service.get_weather()
print(saved_weather_data)

# Example: Clear saved weather data
weather_service.clear_weather()
```

Make sure to replace `'your_api_key'`, `latitude`, and `longitude` with your actual OpenWeatherMap API key and geographical coordinates.

Feel free to explore and customize the provided classes based on your application's requirements.

Happy weather data retrieval!