"""
This module provides an enumeration for different types of weather requests.

Classes:
    RequestType: Enumeration representing different types of weather requests.
"""
from enum import Enum


class RequestType(Enum):
    """Enumeration representing different types of weather requests.

    Attributes:
        current (str): Represents the request for current weather conditions.
        forecast (str): Represents the request for weather forecast information.
    """

    current = 'weather'
    forecast = 'forecast'
