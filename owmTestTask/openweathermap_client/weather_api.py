"""weather_api.py module.

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
import logging
from typing import Any, Dict, Optional
from urllib.parse import urlencode, urljoin

import requests


class WeatherApi(object):
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
        endpoint_url: str = 'https://api.openweathermap.org/data/2.5/',
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

        url_with_endpoint = urljoin(self.endpoint_url, endpoint)
        encoded_params = urlencode({**arguments, 'appid': self.api_key})
        url = urljoin(url_with_endpoint, '?' + encoded_params)

        try:
            if method.upper() == 'GET':
                response = requests.get(url, timeout=self.timeout)
            elif method.upper() == 'POST':
                response = requests.post(url, timeout=self.timeout)
            else:
                raise ValueError("Invalid HTTP method. Use 'GET' or 'POST'.")

            response.raise_for_status()  # Raise an HTTPError for bad responses

            return response.json()
        except requests.exceptions.RequestException as ex:
            logging.error(
                f'Error occurred while making {method} request to {url}. '
                f'Status code: {getattr(ex, "response", None).status_code if hasattr(ex, "response") else None}, '
                f'Reason: {ex.reason if hasattr(ex, "reason") else None}'
            )
            return None
        except Exception as ex:
            logging.error(f'An unexpected error occurred: {str(ex)}')
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
