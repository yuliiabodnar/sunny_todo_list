from django.db import models
from locations.weather.factory.request_weather_factory import RequestWeatherFactory
from locations.weather.factory.weather_factory import WeatherFactory


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

    def get_location_weather_factory(self, request=None):
        """
        Retrieve weather data for the location from an external API.

        Returns:
            Weather: Weather object.
        """
        if request:
            return RequestWeatherFactory(request, self.name)
        else:
            return WeatherFactory()
