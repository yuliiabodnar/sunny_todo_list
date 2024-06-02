from locations.weather.weather import Weather


class WeatherFactory:

    def create(self, location, temperature, is_rain=False, is_cloudy=False, is_sunny=False):
        return Weather(location, temperature, is_rain, is_cloudy, is_sunny)
