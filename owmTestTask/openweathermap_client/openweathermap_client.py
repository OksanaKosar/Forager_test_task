"""openweathermap_client.py module.

This module provides a client for interacting with the OpenWeatherMap API to retrieve weather information.
Classes:

    OpenWeatherMapClient:
        A client for interacting with the OpenWeatherMap API.

Example:
    api_key='your_api_key'
    weather_service = WeatherApiService
    request_handler = WeatherApiService(api_key)
    client = OpenWeatherMapClient(weather_service)
    current_weather = client.get_current_weather(lat='48.92', lon='24.71')
    forecast = client.get_five_days_forecast(lat='48.92', lon='24.71')

"""

from typing import Any, Dict, Optional

from owmTestTask.openweathermapapi_service.openweathermapapi_service import WeatherApiService


class OpenWeatherMapClient(object):
    """
    A client for interacting with the OpenWeatherMap API to retrieve weather information.

    Attributes:
        request_handler (ApiRequestHandler): Handler for making API requests.

    Methods:
        get_current_weather(lat: str, lon: str) -> Optional[Dict[str, Any]]:
            Get the current weather based on latitude and longitude.

        get_five_days_forecast(lat: str, lon: str) -> Optional[Dict[str, Any]]:
            Get a five-day weather forecast based on latitude and longitude.
    """

    def __init__(self, weather_service: WeatherApiService = None) -> None:
        """
        Initialize the OpenWeatherMapClient.

        Args:
            weather_service (WeatherApiService): Service for making API requests.
        """
        self.weather_service = weather_service or WeatherApiService()

    def get_current_weather(self, lat: str, lon: str) -> Optional[Dict[str, Any]]:
        """
        Get the current weather based on latitude and longitude.

        Args:
            lat (str): The latitude of the location.
            lon (str): The longitude of the location.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the current weather information,
                                      or None if the request was unsuccessful.
        """
        coordinates = {'lat': lat, 'lon': lon}
        return self.weather_service.get_request('weather', coordinates)

    def get_five_days_forecast(self, lat: str, lon: str) -> Optional[Dict[str, Any]]:
        """
        Get a five-day weather forecast based on latitude and longitude.

        Args:
            lat (str): The latitude of the location.
            lon (str): The longitude of the location.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the current weather information,
                                      or None if the request was unsuccessful.
        """
        coordinates = {'lat': lat, 'lon': lon}
        return self.weather_service.get_request('forecast', coordinates)
