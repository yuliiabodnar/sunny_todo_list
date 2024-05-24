# tasks/services/weather_service.py
import urllib.request
import json


def _map_weather_response(location, response):
    mapped_data = {'location': location}

    # Validate response structure and extract data if available
    if "main" in response and "temp" in response["main"]:
        mapped_data['temp'] = response["main"]["temp"]
    else:
        # Set temp to None if not available or invalid
        mapped_data['temp'] = None

    if "weather" in response and response["weather"]:
        mapped_data['main'] = response["weather"][0].get("main", None)
        mapped_data['icon'] = response["weather"][0].get("icon", None)
    else:
        # Set main and icon to None if weather data is missing
        mapped_data['main'] = None
        mapped_data['icon'] = None

    return mapped_data


class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key

    def _construct_api_url(self, location):
        # Construct the URL for the weather API using the location and API key
        return f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={self.api_key}'

    def get_weather_data(self, location):
        # Get the API URL
        url = self._construct_api_url(location)

        try:
            # Make a request to the weather API and read the response
            source = urllib.request.urlopen(url.format(location)).read()

            # Parse the JSON response
            res = json.loads(source)

            # Map the weather response to a structured format
            return _map_weather_response(location, res)
        except Exception as e:
            # If an exception occurs during API request or response parsing, return an error message
            return {'error': str(e)}
