from django.db import models
from locations.weather.weather_service import WeatherService
from locations.weather.weather_parser import WeatherParser


class Location(models.Model):
    """
    A model representing a location.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Return the string representation of the location.
        """
        return self.name

    def get_weather_info(self, request):
        """
        Retrieve weather data for the location from an external API.

        Returns:
            dict: Weather data in JSON format.
        """
        weather_service = WeatherService(request)
        weather_parser = WeatherParser()

        location_weather_info = weather_service.get_weather_info(self.name)
        parsed_weather_info = weather_parser.parse_location_weather_response(self.name, location_weather_info)

        return parsed_weather_info
