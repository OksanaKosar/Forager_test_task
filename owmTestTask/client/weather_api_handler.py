"""weather_api_handler.py module.

This module defines the `WeatherApiHandler` class, which extends the functionality of the `BaseApiHandler` class
to interact specifically with the OpenWeatherMap API.

Classes:
    WeatherApiHandler: A class for handling OpenWeatherMap API requests, inheriting from `BaseApiHandler`.
"""
from typing import Any, Dict, Optional
from urllib.parse import urlencode, urljoin

from owmTestTask.client.api_handler import BaseApiHandler


class WeatherApiHandler(BaseApiHandler):
    """WeatherApiHandler class.

    This class extends BaseApiHandler and is specifically designed for handling weather-related requests
    using the OpenWeatherMap API.

    Attributes:
        api_key (str): The API key required for accessing the OpenWeatherMap API.
        endpoint_url (str): The base URL for the OpenWeatherMap API.

    """

    def __init__(self, api_key: str) -> None:
        """Initialize the WeatherApiHandler with the provided OpenWeatherMap API key and endpoint URL.

        Args:
            api_key (str): The API key required for accessing the OpenWeatherMap API.

        """
        super().__init__()
        self.api_key = api_key
        self.endpoint_url = 'https://api.openweathermap.org/data/2.5/'

    def get_weather_for_city(self, city_name: str) -> Optional[Dict[str, Any]]:
        """Get weather information for a specific city.

        Args:
            city_name (str): The name of the city for which weather information is requested.

        Returns:
            Optional[Dict[str, Any]]: The weather information for the specified city.

        """
        url = self.format_url('weather', city_name)
        return self.get_request(url)

    def get_forecast_for_city(self, city_name: str) -> Optional[Dict[str, Any]]:
        """Get weather forecast for a specific city.

        Args:
            city_name (str): The name of the city for which weather forecast is requested.

        Returns:
            Optional[Dict[str, Any]]: The weather forecast for the specified city.

        """
        url = self.format_url('forecast', city_name)
        return self.get_request(url)

    def format_url(self, endpoint, city_name) -> str:
        """Format the API URL for a specific endpoint and city.

        Args:
            endpoint (str): The specific API endpoint for the request (e.g., 'weather' or 'forecast').
            city_name (str): The name of the city for which the request is being made.

        Returns:
            str: The formatted API URL.

        """
        url_with_endpoint = urljoin(self.endpoint_url, endpoint)
        encoded_params = urlencode({'q': city_name, 'appid': self.api_key})
        return urljoin(url_with_endpoint, '?{0}'.format(encoded_params))
