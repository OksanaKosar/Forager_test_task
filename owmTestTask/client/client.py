"""client.py module.

This module provides a client for interacting with the OpenWeatherMap API to retrieve weather information.
Classes:

    OpenWeatherMapClient:
        A client for interacting with the OpenWeatherMap API.

Example:
    api_key='your_api_key'
    weather_handler = WeatherApiHandler(api_key)
    client = OpenWeatherMapClient(weather_handler)
    forecast = client.weather(request_type=RequestType.CURRENT, lat='48.92', lon='24.71')

"""
from __future__ import annotations

from typing import Any, Dict, Optional

from owmTestTask.client.request_type_enums import RequestType
from owmTestTask.client.weather_api import WeatherApiHandler


class Client(object):
    """OpenWeatherMap Client for retrieving weather information using a provided WeatherApiHandler.

    Attributes:
        weather_handler (WeatherApiHandler): Service for making API requests.

    Methods:
        __init__(self, weather_handler: WeatherApiHandler = None) -> None:
            Initialize the OpenWeatherMapClient.

            Args:
                weather_handler (WeatherApiHandler): Service for making API requests.

        weather(self, request_type: RequestType | str, lat: str, lon: str) -> Optional[Dict[str, Any]]:
            Retrieve weather information for a given location using the specified request type.

            Args:
                request_type (RequestType | str): The type of weather request, either as a RequestType enum or a string.
                lat (str): The latitude of the location.
                lon (str): The longitude of the location.

            Returns:
                Optional[Dict[str, Any]]: A dictionary containing weather information or None if the request fails.
    """

    def __init__(self, weather_handler: WeatherApiHandler = None) -> None:
        """
        Initialize the OpenWeatherMapClient.

        Args:
            weather_handler (WeatherApiHandler): Service for making API requests.
        """
        self.weather_handler = weather_handler

    def weather(
        self, request_type: RequestType | str, lat: str, lon: str,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieve weather information for a given location using the specified request type.

        Args:
            request_type (RequestType | str): The type of weather request, either as a RequestType enum.
            lat (str): The latitude of the location.
            lon (str): The longitude of the location.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing weather information or None if the request fails.
        """
        coordinates = {'lat': lat, 'lon': lon}
        if isinstance(request_type, RequestType):
            request_type = request_type.value
        return self.weather_handler.get_request(request_type, coordinates)
