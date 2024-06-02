from locations.weather.weather_service import WeatherService
from locations.weather.weather_parser import WeatherParser


class RequestWeatherFactory:

    def __init__(self, request, location_name):
        """
        Initialize the WeatherAPI object.

        Args:
            request (HttpRequest): The HTTP request object.
        """
        self.request = request
        self.location_name = location_name

    def create(self):
        """
        Retrieve weather data for the location from an external API.

        Returns:
            Weather: Weather object.
        """
        weather_service = WeatherService(self.request)
        weather_parser = WeatherParser()

        location_weather_info = weather_service.get_weather_info(self.location_name)
        location_weather = weather_parser.parse_location_weather_response(self.location_name, location_weather_info)

        return location_weather
