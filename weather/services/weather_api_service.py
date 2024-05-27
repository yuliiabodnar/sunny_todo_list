# weather/weather/weather_service.py
import urllib.request
import json


class WeatherAPIService:
    def __init__(self, api_key):
        """
        Initialize the WeatherService with the provided API key.

        Args:
            api_key (str): The API key for accessing the weather service.
        """
        self.api_key = api_key

    def _construct_api_url(self, location):
        """
        Construct the URL for the weather API using the location and API key.

        Args:
            location (str): The location for which weather data is requested.

        Returns:
            str: The constructed API URL.
        """
        return f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={self.api_key}'

    def get_weather_data(self, location):
        """
        Get weather data for the specified location.

        Args:
            location (str): The location for which weather data is requested.

        Returns:
            dict: Weather information in a structured format.
        """
        # Get the API URL
        url = self._construct_api_url(location)

        try:
            # Make a request to the weather API and read the response
            source = urllib.request.urlopen(url.format(location)).read()

            # Parse and return the JSON response
            return json.loads(source)

        except Exception as e:
            # If an exception occurs during API request or response parsing, return an error message
            return {'error': str(e)}
