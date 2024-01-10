"""weather_api_handler.py module.

This module defines the `WeatherApiHandler` class, which extends the functionality of the `BaseApiHandler` class
to interact specifically with the OpenWeatherMap API.

Classes:
    WeatherApiHandler: A class for handling OpenWeatherMap API requests, inheriting from `BaseApiHandler`.
"""
from urllib.parse import urlencode, urljoin

from owmTestTask.client.api_handler import BaseApiHandler


class WeatherApiHandler(BaseApiHandler):
    """Weather API Handler Class.

    This class extends the functionality of the `BaseApiHandler` class to interact specifically
    with the OpenWeatherMap API.

    Attributes:
        api_key (str): The API key for accessing the OpenWeatherMap API.
        endpoint (str): The specific API endpoint for weather data.
        lat (str): The latitude coordinate for the weather location.
        lon (str): The longitude coordinate for the weather location.
        endpoint_url (str): The base URL for the OpenWeatherMap API.
        coordinates (dict): A dictionary containing latitude and longitude coordinates.
    """

    def __init__(self, api_key: str, endpoint: str, lat: str, lon: str) -> None:
        """Initialize the WeatherApiHandler with the provided OpenWeatherMap API key and endpoint URL.

        Attributes:
            api_key (str): The API key for accessing the OpenWeatherMap API.
            endpoint (str): The specific API endpoint for weather data.
            lat (str): The latitude coordinate for the weather location.
            lon (str): The longitude coordinate for the weather location.
        """
        super().__init__()
        self.api_key = api_key
        self.endpoint_url = 'https://api.openweathermap.org/data/2.5/'
        self.endpoint = endpoint
        self.coordinates = {'lat': lat, 'lon': lon}

    def format_url(self) -> str:
        """Format the API URL.

        This method formats the API URL by combining the base URL, endpoint, and
        query parameters including latitude, longitude, and API key.

        Returns:
            str: The formatted API URL.

        """
        url_with_endpoint = urljoin(self.endpoint_url, self.endpoint)
        encoded_params = urlencode({**self.coordinates, 'appid': self.api_key})
        return urljoin(url_with_endpoint, '?{0}'.format(encoded_params))
