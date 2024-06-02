from locations.weather.weather import Weather


class WeatherParser:
    """
        WeatherParser is responsible for parsing weather data for a given location.
    """
    def parse_location_weather_response(self, location, weather_data):
        """
        Parses weather data for a given location and returns a Weather object.

        Args:
            location (str):      The name of the location for which the weather data is provided.
            weather_data (dict): The weather data dictionary containing 'temp', 'main', and 'icon' keys.

        Returns:
            Weather: An instance of the Weather class populated with the parsed data.
        """
        is_cloudy = False
        is_rain = False
        is_sunny = False

        # Validate the presence of weather_data
        if not weather_data:
            raise ValueError("Weather data is required")

        temperature = weather_data.get('temp')
        main = weather_data.get('main')
        icon = weather_data.get('icon')

        # Validate the required fields in weather_data
        if temperature is None:
            raise ValueError("Temperature is missing in weather data")
        if main is None:
            raise ValueError("Main weather condition is missing in weather data")
        if icon is None:
            raise ValueError("Weather icon is missing in weather data")

        # Set weather condition flags based on the 'main' and 'icon' values
        if main == 'Clouds':
            is_cloudy = True
        if main == 'Rain':
            is_rain = True
        if main == 'Clear' and icon == '01d':
            is_sunny = True

        # Return the Weather object with the parsed data
        return Weather(location, temperature, is_rain, is_cloudy, is_sunny)
