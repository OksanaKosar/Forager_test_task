"""weather_client.py module.

This module defines the WeatherClient class, which is used for interacting with the OpenWeatherMap API.

"""
from owmTestTask.client.weather_api_handler import WeatherApiHandler


class WeatherClient(object):
    """This class provides a client interface for accessing weather information through the OpenWeatherMap API.

    Attributes:
        weather_handler (WeatherApiHandler): An instance of WeatherApiHandler for handling weather-related API requests.

    """

    def __init__(self, api_key: str) -> None:
        """Initialize the WeatherClient.

        Args:
            api_key (str): The API key required for accessing the OpenWeatherMap API.

        """
        self.weather_handler = WeatherApiHandler(api_key=api_key)
