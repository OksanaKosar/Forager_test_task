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
