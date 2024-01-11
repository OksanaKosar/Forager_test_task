"""api_handler.py module.

This module defines the `BaseApiHandler` class, which serves as a base class for handling API requests.

Classes:
    BaseApiHandler: A base class for handling API requests.
"""
from typing import Any, Dict, Optional

import requests


class BaseApiHandler(object):
    """
    Base class for handling API requests.

    Args:
        timeout (int, optional): The timeout value for the HTTP requests in seconds (default is 5).

    Methods:
        send_request(url: str, method: str) -> Optional[Dict[str, Any]]:
            Sends an HTTP request to the specified url with the given arguments using the specified HTTP method.

        post_request(url: str) -> Optional[Dict[str, Any]]:
            Sends a POST request to the specified url with the given arguments.

        get_request(url: str) -> Optional[Dict[str, Any]]:
            Sends a GET request to the specified url with the given arguments.
    """

    def __init__(
        self,
        timeout: int = 5,
    ) -> None:
        """Initialize the BaseApiHandler with the provided API key, endpoint URL, and timeout.

        Args:
            timeout (int): The timeout value for the HTTP requests in seconds (default is 5).
        """
        self.timeout = timeout

    def send_request(
        self,
        url: str,
        method: str,
    ) -> Optional[Dict[str, Any]]:
        """Send an HTTP request to the specified endpoint with the given arguments using the specified HTTP method.

        Args:
            url (str): url for the request
            method (str): The HTTP method to use for the request (e.g., 'GET' or 'POST').

        Returns:
            Optional[Dict[str, Any]]: The JSON response from the API, or None if the request was unsuccessful.
        """
        response = requests.request(method, url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def post_request(self, url) -> Optional[Dict[str, Any]]:
        """Send a POST request to the specified endpoint with the given arguments.

        Args:
            url (str): url for the request

        Returns:
            Optional[Dict[str, Any]]: The JSON response from the API, or None if the request was unsuccessful.
        """
        return self.send_request(url, method='POST')

    def get_request(self, url) -> Optional[Dict[str, Any]]:
        """Send a GET request to the specified endpoint with the given arguments.

        Args:
            url (str): url for the request

        Returns:
            Optional[Dict[str, Any]]: The JSON response from the API, or None if the request was unsuccessful.
        """
        return self.send_request(url, method='GET')
