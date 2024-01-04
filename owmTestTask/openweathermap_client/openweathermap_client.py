"""openweathermap_client.py module.
This module provides a client for interacting with the OpenWeatherMap API to retrieve weather information.

Classes:
    ApiRequestHandler:
        Handles API requests to the OpenWeatherMap API.

    OpenWeatherMapClient:
        A client for interacting with the OpenWeatherMap API.

Attributes:
    __version__ (str): The version of the OpenWeatherMapClient module.

Example:
    request_handler = ApiRequestHandler()
    client = OpenWeatherMapClient(api_key='your_api_key', request_handler=request_handler)
    current_weather = client.get_current_weather(lat='37.7749', lon='-122.4194')
    forecast = client.get_five_days_forecast(lat='37.7749', lon='-122.4194')

"""

import logging
from typing import Any, Dict, Optional

import requests


class ApiRequestHandler(object):
    """
    Handles API requests to the OpenWeatherMap API.

    Attributes:
        endpoint_url (str): The base URL for OpenWeatherMap API endpoints.
        timeout (int): Timeout for API requests.

    Methods:
        make_request(endpoint: str, params: Dict[str, str], api_key: str) -> Optional[Dict[str, Any]]:
            Make a request to the OpenWeatherMap API.
    """

    def __init__(self, endpoint_url: str = 'https://api.openweathermap.org/data/2.5', timeout: int = 5) -> None:
        """
        Initialize the ApiRequestHandler.

        Args:
            endpoint_url (str): The base URL for OpenWeatherMap API endpoints.
            timeout (int): Timeout for API requests.
        """
        self.endpoint_url = endpoint_url
        self.timeout = timeout

    def make_request(
        self, endpoint: str, arguments: Dict[str, str], api_key: str,
    ) -> Optional[Dict[str, Any]]:
        """Make a request to the OpenWeatherMap API.

        Args:
            endpoint (str): The API endpoint.
            arguments (Dict[str, str]): Parameters for the API request.
            api_key (str): The API key required for authentication.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the API response,
                                      or None if the request was unsuccessful.
        """
        try:
            response = requests.get(
                '{0}/{1}'.format(self.endpoint_url, endpoint),
                params={**arguments, 'appid': api_key},
                timeout=self.timeout,
            )
        except requests.RequestException as exep:
            logging.error('RequestException: {0}'.format(exep))
            return None

        if response.ok:
            return response.json()
        logging.error('Error: {0} - {1}'.format(response.status_code, response.text))
        return None


class OpenWeatherMapClient(object):
    """
    A client for interacting with the OpenWeatherMap API to retrieve weather information.

    Attributes:
        api_key (str): The API key required for authentication.
        request_handler (ApiRequestHandler): Handler for making API requests.

    Methods:
        get_current_weather(lat: str, lon: str) -> Optional[Dict[str, Any]]:
            Get the current weather based on latitude and longitude.

        get_five_days_forecast(lat: str, lon: str) -> Optional[Dict[str, Any]]:
            Get a five-day weather forecast based on latitude and longitude.
    """

    def __init__(self, api_key: str, request_handler: ApiRequestHandler = None) -> None:
        """
        Initialize the OpenWeatherMapClient.

        Args:
            api_key (str): The API key required for authentication.
            request_handler (ApiRequestHandler): Handler for making API requests.
        """
        self.api_key = api_key
        self.request_handler = request_handler or ApiRequestHandler()
        self.logger = logging.getLogger(__name__)

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
        return self.request_handler.make_request('weather', coordinates, self.api_key)

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
        return self.request_handler.make_request('forecast', coordinates, self.api_key)
