from django.http import JsonResponse


class WeatherParser:

    def get_color_for_location(self, weather_data):
        # Determine the background color based on weather data
        background_class = None
        if weather_data:
            temperature = weather_data.get('temp')
            if temperature is not None:
                if temperature < 10:
                    background_class = 'task-cold'  # Cold temperature
                elif temperature >= 10 and temperature < 20:
                    background_class = 'task-moderate'  # Moderate temperature
                else:
                    background_class = 'task-warm'  # Warm temperature

        return background_class

    def parse_location_weather_response(self, location, weather_data):

        location_data = {}

        if weather_data:
            location_data = {
                'location': location,
                'temperature': weather_data.get('temp'),
                'background_class': self.get_color_for_location(weather_data)
            }

        return location_data
