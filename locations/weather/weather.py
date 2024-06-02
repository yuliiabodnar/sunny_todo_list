class Weather:
    def __init__(self, location, temperature, is_rain, is_cloudy, is_sunny):
        """
        Initialize the Weather object.

        Args:
            location (str): The location for the weather.
            temperature (float): The temperature at the location.
            is_rain (bool): Whether it is raining at the location.
            is_cloudy (bool): Whether it is cloudy at the location.
            is_sunny (bool): Whether it is sunny at the location.
        """
        self.location = location
        self.temperature = temperature
        self.is_rain = is_rain
        self.is_cloudy = is_cloudy
        self.is_sunny = is_sunny
