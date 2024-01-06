"""weather_api_service.py.

Module providing a simple wrapper class for interacting with the OpenWeatherMap API.

Usage:
    1. Create an instance of WeatherApiService by providing the API key.
    2. Use the provided methods to make GET or POST requests to the OpenWeatherMap API.

Example:
    api_key = 'your_openweathermap_api_key'
    weather_service = WeatherApiService(api_key)
    client = OpenWeatherMapClient(weather_service)
    current_weather = client.get_current_weather(lat='48.92', lon='24.71')
    forecast = client.get_five_days_forecast(lat='48.92', lon='24.71')
"""
import json
import logging
from typing import Any, Dict, Optional
from urllib import parse, request

import requests


class WeatherApiService(object):
    """
    Handles API requests to the OpenWeatherMap API.

    Attributes:
        api_key (str): The API key required for authentication.
        endpoint_url (str): The base URL for OpenWeatherMap API endpoints.
        timeout (int): Timeout for API requests.

    Methods:
        get_request(endpoint: str, params: Dict[str, str]) -> Optional[Dict[str, Any]]:
        Get a request to the OpenWeatherMap API.
        post_request(endpoint: str, params: Dict[str, str]) -> Optional[Dict[str, Any]]:
        Post a request to the OpenWeatherMap API.
    """

    def __init__(
            self,
            api_key: str,
            endpoint_url: str = 'https://api.openweathermap.org/data/2.5',
            timeout: int = 5,
    ) -> None:
        """
        Initialize the WeatherApiService.

        Args:
            api_key (str): The API key required for authentication.
            endpoint_url (str): The base URL for OpenWeatherMap API endpoints.
            timeout (int): Timeout for API requests.
        """
        self.api_key = api_key
        self.endpoint_url = endpoint_url
        self.timeout = timeout

    def post_request(
            self, endpoint: str, arguments: Dict[str, str],
    ) -> Optional[Dict[str, Any]]:
        """
        Perform a POST request to the OpenWeatherMap API.

        Args:
            endpoint (str): The API endpoint to which the request will be sent.
            arguments (Dict[str, str]): The request parameters.

        Returns:
            Optional[Dict[str, Any]]: The JSON response if the request is successful, else None.
        """
        try:
            url = '{0}/{1}?{2}'.format(self.endpoint_url, endpoint,
                                       parse.urlencode({**arguments, 'appid': self.api_key}))
            req = request.Request(url, method='POST')
            with request.urlopen(req, timeout=self.timeout) as response:
                data = response.read()
                return json.loads(data.decode('utf-8')) if response.status == 200 else None
        except request.URLError as ex:
            logging.error('URLError: {0}'.format(ex))
            return None

    def get_request(self, endpoint: str, arguments: Dict[str, str]) -> Optional[Dict[str, Any]]:
        """
        Perform a GET request to the OpenWeatherMap API.

        Args:
            endpoint (str): The API endpoint to which the request will be sent.
            arguments (Dict[str, str]): The request parameters.

        Returns:
            Optional[Dict[str, Any]]: The JSON response if the request is successful, else None.
        """
        try:
            url = '{0}/{1}?{2}'.format(self.endpoint_url, endpoint,
                                       parse.urlencode({**arguments, 'appid': self.api_key}))
            req = request.Request(url, method='GET')
            with request.urlopen(req, timeout=self.timeout) as response:
                data = response.read()
                return json.loads(data.decode('utf-8')) if response.status == 200 else None
        except request.URLError as ex:
            logging.error('URLError: {0}'.format(ex))
            return None

