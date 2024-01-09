"""client.py module.

This module contains a Client class that interacts with a weather API using a provided WeatherApiHandler.
Classes:

    Client:
        A client for interacting with the OpenWeatherMap API.

Example:
    api_key='your_api_key'
    weather_handler = WeatherApiHandler(api_key)
    client = OpenWeatherMapClient(lat='48.92', lon='24.71', weather_handler)
    forecast = client.current_weather

"""

from typing import Any, Dict, Optional

from owmTestTask.client.weather_api import WeatherApiHandler


class Client(object):
    """
    Client class for interacting with a weather API using a specified WeatherApiHandler.

    Attributes:
        coordinates (Dict[str, str]): A dictionary containing latitude ('lat') and longitude ('lon').
        weather_handler (WeatherApiHandler): Service for making API requests.
        current_weather (Optional[Dict[str, Any]]): Current weather information retrieved from the API.
        five_days_forecast (Optional[Dict[str, Any]]): Five days forecast information retrieved from the API.

    """

    def __init__(self, lat: str, lon: str, weather_handler: WeatherApiHandler = None) -> None:
        """Initialize the Client.

        Args:
            lat (str): Latitude.
            lon (str): Longitude.
            weather_handler (WeatherApiHandler): Service for making API requests.

        """
        self.coordinates = {'lat': lat, 'lon': lon}
        self.weather_handler = weather_handler
        self.current_weather = self.weather_handler.get_request('weather', self.coordinates)
        self.five_days_forecast = self.weather_handler.get_request('forecast', self.coordinates)

    @property
    def current_weather(self) -> Optional[Dict[str, Any]]:
        """Get the current weather information.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing current weather information.

        """
        return self._current_weather

    @property
    def five_days_forecast(self) -> Optional[Dict[str, Any]]:
        """Get the five days forecast information.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing five days forecast information.

        """
        return self._five_days_forecast

    @current_weather.setter
    def current_weather(self, value_weather):
        self._current_weather = value_weather

    @five_days_forecast.setter
    def five_days_forecast(self, value_weather):
        self._five_days_forecast = value_weather
