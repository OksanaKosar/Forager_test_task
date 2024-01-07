"""openweathermap_service.py module.

This module provides a class for interacting with the OpenWeatherMap API and saving weather data.

Classes:
    OpenWeatherMapService:
        A class for interacting with the OpenWeatherMap API and managing weather data.

Attributes:
    None

Methods:
    __init__():
        Initialize the OpenWeatherMapService.

    save_weather(response: dict) -> None:
        Save weather data from the API response.

    get_weather() -> list:
        Retrieve the stored weather data.

    clear_weather() -> None:
        Clear the stored weather data.
"""


class OpenWeatherMapService(object):
    """
    A class for interacting with the OpenWeatherMap API and saving weather data.

    Attributes:
        results (list): A list to store the retrieved weather data.

    Methods:
        save_weather(response: dict) -> None:
            Save weather data from the API response.

        get_weather() -> list:
            Retrieve the stored weather data.

        clear_weather() -> None:
            Clear the stored weather data.
    """

    def __init__(self, db):
        """
        Initialize the OpenWeatherMapService.

        The results attribute is set to an empty list.
        """
        self.db = db

    def save_weather(self, response: dict) -> None:
        """
        Save weather data from the API response.

        Args:
            response (dict): The API response containing weather data.
        """
        if 'list' in response:
            city_name = response['city']['name']
            for weather in response.get('list'):
                if '15:00:00' in weather['dt_txt']:
                    response_dict = {
                        'name': city_name,
                        'data': weather['dt_txt'],
                        'description': weather['weather'][0]['description'],
                        'temp': str(weather['main']['temp']),
                    }
                    self.db.add_data(response_dict)
        else:
            response_dict = {
                'name': response['name'],
                'description': response['weather'][0]['description'],
                'temp': str(response['main']['temp']),
            }
            self.db.add_data(response_dict)

    def get_weather(self) -> list:
        """
        Retrieve the stored weather data.

        Returns:
            list: A list containing stored weather data.
        """
        return self.db.db_content

    def clear_weather(self) -> None:
        """Clear the stored weather data."""
        self.db.clear_data()



