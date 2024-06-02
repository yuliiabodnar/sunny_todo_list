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

    class Meta:
        app_label = 'locations'

    def get_location_weather(self, request=None):
        """
        Retrieve weather data for the location from an external API.

        Returns:
            Weather: Weather object.
        """
        weather_service = WeatherService(request)
        weather_parser = WeatherParser()

        location_weather_info = weather_service.get_weather_info(self.name)
        location_weather = weather_parser.parse_location_weather_response(self.name, location_weather_info)

        return location_weather
