"""weatherapi_service.py module.

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
from urllib.error import HTTPError


class WeatherApiService(object):
    """
    A service class for interacting with the OpenWeatherMap API.

    This class provides methods to send HTTP requests (GET and POST) to OpenWeatherMap API
    endpoints and retrieve weather-related information.

    Attributes:
        - api_key (str): The API key required for authentication.
        - endpoint_url (str): The base URL for OpenWeatherMap API endpoints.
        - timeout (int): Timeout for API requests.

    Methods:
        - send_request(endpoint, arguments, method): Send an HTTP request to the OpenWeatherMap API.
        - post_request(endpoint, arguments): Send a POST request to the OpenWeatherMap API.
        - get_request(endpoint, arguments): Send a GET request to the OpenWeatherMap API.
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
        self.status_ok = 200

    def send_request(
        self, endpoint: str, arguments: Dict[str, str], method: str,
    ) -> Optional[Dict[str, Any]]:
        """
        Send an HTTP request to the OpenWeatherMap API.

        Parameters:
            - endpoint (str): The API endpoint to request.
            - arguments (Dict[str, str]): The query parameters for the request.
            - method (str): The HTTP method to use ('GET' or 'POST').
        Returns:
            Optional[Dict[str, Any]]: The JSON response as a dictionary if the request is successful, otherwise None.
        """
        url = '{0}/{1}?{2}'.format(
            self.endpoint_url, endpoint, parse.urlencode({**arguments, 'appid': self.api_key}),
        )
        req = request.Request(url, method=method)

        try:
            with request.urlopen(req, timeout=self.timeout) as response:
                data_response = response.read()
                if response.status == self.status_ok:
                    return json.loads(data_response.decode('utf-8'))
                return None
        except HTTPError as ex:
            logging.error(
                'Error occurred while making {0} request to {1}. Status code: {2}, Reason: {3}'.format(
                    method, url, ex.code, ex.reason,
                ))
            return None
        except Exception as ex:
            logging.error('An unexpected error occurred: {0}'.format(str(ex)))
            return None

    def post_request(
        self, endpoint: str, arguments: Dict[str, str],
    ) -> Optional[Dict[str, Any]]:
        """
        Send a POST request to the OpenWeatherMap API.

        Parameters:
            - endpoint (str): The API endpoint to request.
            - arguments (Dict[str, str]): The query parameters for the request.

        Returns:
            Optional[Dict[str, Any]]: The JSON response as a dictionary if the request is successful, otherwise None.
        """
        return self.send_request(endpoint, arguments, method='POST')

    def get_request(
        self, endpoint: str, arguments: Dict[str, str],
    ) -> Optional[Dict[str, Any]]:
        """
        Send a GET request to the OpenWeatherMap API.

        Parameters:
            - endpoint (str): The API endpoint to request.
            - arguments (Dict[str, str]): The query parameters for the request.

        Returns:
            Optional[Dict[str, Any]]: The JSON response as a dictionary if the request is successful, otherwise None.
        """
        return self.send_request(endpoint, arguments, method='GET')
