"""db.py module.

This module defines a simple class for storing and managing local data.

Classes:
    DB: A class representing a simple local database.

Usage:
    To use this module, create an instance of the DB class and interact with its methods.

Classes and Methods:
    DB:
        - __init__(): Initializes an instance of the DB class.
        - add_data(db_content: dict): Adds data to the local database.
        - clear_data(): Clears all stored data in the database.
        - db_content: A property to retrieve all data stored in the database.

Note:
    This module provides a basic local storage solution and is intended for simple use cases.
"""


class DB(object):
    """Simple class for storing locally data."""

    def __init__(self):
        """
        Initialize the OpenWeatherMapService.

        The results attribute is set to an empty list.
        """
        self._db_content = []

    def add_data(self, db_content: dict):
        """Add data to DB."""
        self._db_content.append(db_content)

    def clear_data(self):
        """Clear the stored data."""
        self._db_content = []

    @property
    def db_content(self) -> list:
        """Retrieve all data stored in DB.

        Returns:
            list: A list containing stored data.
        """
        return self._db_content
