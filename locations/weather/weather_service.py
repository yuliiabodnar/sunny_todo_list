import requests
from urllib.parse import urlencode, urlunparse
from django.urls import reverse


class WeatherService:
    """
    A class to interact with a weather API and retrieve weather data.
    """

    def __init__(self, request):
        """
        Initialize the WeatherAPI object.

        Args:
            request (HttpRequest): The HTTP request object.
        """
        self.request = request

    def _generate_weather_url(self, endpoint, params):
        """
        Generate the URL for retrieving weather data for the given location.

        Args:
            endpoint (str): The endpoint for which weather data is requested.
            params (dict):  The query parameters to include in the URL.

        Returns:
            str: The generated URL for retrieving weather data.
        """
        try:
            # Use reverse to get the relative URL for the given endpoint
            weather_path = reverse(endpoint)

            # Build the full base URL using request.scheme and request.get_host
            full_base_url = f"{self.request.scheme}://{self.request.get_host()}"
            weather_url = f"{full_base_url}{weather_path}"

            # Encode query parameters
            query_string = urlencode(params)

            # Build the full URL with query parameters using urlunparse
            full_url = urlunparse((self.request.scheme, self.request.get_host(), weather_path, '', query_string, ''))

            return full_url
        except Exception as e:
            # Handle any errors that occur during URL generation
            print(f"Error generating weather URL: {e}")
            return None

    def get_weather_info(self, location):
        """
        Retrieve weather data for the specified location.

        Args:
            location (str): The location for which weather data is requested.

        Returns:
            dict: Weather data in JSON format.
        """
        try:
            # Generate the weather URL
            endpoint = 'weather:get'
            params = {'location': location}
            url = self._generate_weather_url(endpoint, params)

            if url:
                # Make a GET request to the weather URL
                response = requests.get(url)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Parse the JSON response and return weather data
                    return response.json()

                # Handle unsuccessful request (e.g., return None or raise an exception)
            return None
        except Exception as e:
            # Handle any other errors
            print(f"Error fetching weather data: {e}")
            return None
