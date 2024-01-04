"""open_weather_map_client.py module.

This module provides a client for interacting with the OpenWeatherMap API to retrieve weather information.

Classes:
    OpenWeatherMapClient:
        A client for interacting with the OpenWeatherMap API.

Attributes:
    __version__ (str): The version of the OpenWeatherMapClient module.

Example:
    client = OpenWeatherMapClient(api_key='your_api_key')
    current_weather = client.get_current_weather(lat='37.7749', lon='-122.4194')
    forecast = client.get_five_days_forecast(lat='37.7749', lon='-122.4194')
"""

from typing import Any, Dict, Optional

import requests


class OpenWeatherMapClient(object):
    """
    A client for interacting with the OpenWeatherMap API to retrieve weather information.

    Attributes:
        api_key (str): The API key required for authentication.

    Methods:
        get_current_weather(lat: str, lon: str) -> Optional[Dict[str, Any]]:
            Get the current weather based on latitude and longitude.

        get_five_days_forecast(lat: str, lon: str) -> Optional[Dict[str, Any]]:
            Get a five-day weather forecast based on latitude and longitude.
    """

    def __init__(self, api_key: str) -> None:
        """
        Initialize the OpenWeatherMapClient.

        Args:
            api_key (str): The API key required for authentication.
        """
        self.api_key = api_key

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
        response = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid={2}'.format(lat, lon, self.api_key),
            timeout=5,
        )
        return response.json() if response.ok else None

    def get_five_days_forecast(self, lat: str, lon: str) -> Optional[Dict[str, Any]]:
        """
        Get the current weather based on latitude and longitude.

        Args:
            lat (str): The latitude of the location.
            lon (str): The longitude of the location.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the current weather information,
                                      or None if the request was unsuccessful.
        """
        response = requests.get(
            'https://api.openweathermap.org/data/2.5/forecast?lat={0}&lon={1}&appid={2}'.format(lat, lon, self.api_key),
            timeout=5,
        )
        return response.json() if response.ok else None
