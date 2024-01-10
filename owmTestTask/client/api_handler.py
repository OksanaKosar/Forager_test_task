"""api_handler.py module.

This module defines the `BaseApiHandler` class, which serves as a base class for handling API requests.

Classes:
    BaseApiHandler: A base class for handling API requests.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

import requests


class BaseApiHandler(ABC):
    """
    Base class for handling API requests.

    Args:
        timeout (int, optional): The timeout value for the HTTP requests in seconds (default is 5).

    Methods:
        send_request(endpoint: str, arguments: Dict[str, str], method: str) -> Optional[Dict[str, Any]]:
            Sends an HTTP request to the specified endpoint with the given arguments using the specified HTTP method.

        post_request(endpoint: str, arguments: Dict[str, str]) -> Optional[Dict[str, Any]]:
            Sends a POST request to the specified endpoint with the given arguments.

        get_request(endpoint: str, arguments: Dict[str, str]) -> Optional[Dict[str, Any]]:
            Sends a GET request to the specified endpoint with the given arguments.

        format_url() -> str:
            Forms the url for the request.
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

    @abstractmethod
    def format_url(self):
        """Abstract method to format the API URL.

        This method should be implemented by subclasses to define how the API URL
        should be formatted.

        Returns:
            str: The formatted API URL.

        """
        raise NotImplementedError('Subclasses must implement this method.')

    def send_request(
        self,
        method: str,
    ) -> Optional[Dict[str, Any]]:
        """Send an HTTP request to the specified endpoint with the given arguments using the specified HTTP method.

        Args:
            method (str): The HTTP method to use for the request (e.g., 'GET' or 'POST').

        Returns:
            Optional[Dict[str, Any]]: The JSON response from the API, or None if the request was unsuccessful.
        """
        url = self.format_url()
        response = requests.request(method, url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def post_request(self) -> Optional[Dict[str, Any]]:
        """Send a POST request to the specified endpoint with the given arguments.

        Returns:
            Optional[Dict[str, Any]]: The JSON response from the API, or None if the request was unsuccessful.
        """
        return self.send_request(method='POST')

    def get_request(self) -> Optional[Dict[str, Any]]:
        """Send a GET request to the specified endpoint with the given arguments.

        Returns:
            Optional[Dict[str, Any]]: The JSON response from the API, or None if the request was unsuccessful.
        """
        return self.send_request(method='GET')
