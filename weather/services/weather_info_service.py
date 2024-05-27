# weather/weather/weather_info_service.py
from .weather_api_service import WeatherAPIService


def _map_weather_response(location, response):
    """
    Map the weather API response to a structured format.

    Args:
        location (str):  The location for which weather data is requested.
        response (dict): The weather API response.

    Returns:
        dict: Weather information in a structured format.
    """
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


def get_weather_info(location, api_key):
    """
    Retrieve weather information for the specified location.

    Args:
        location (str): The location for which weather data is requested.
        api_key (str):  The API key for accessing the weather service.

    Returns:
        tuple: A tuple containing weather information in a structured format
            and the corresponding status code.
    """
    if not location:
        # If location parameter is missing, return error response
        return {'error': 'Location parameter is missing'}, 400

    # Initialize WeatherService with the API key
    weather_api_service = WeatherAPIService(api_key)

    # Get weather information for the specified location
    res = weather_api_service.get_weather_data(location)

    # Map the weather response to a structured format
    weather_info = _map_weather_response(location, res)

    # Check for any errors in weather data retrieval
    if 'error' in weather_info:
        # If weather data retrieval failed, return error response
        return {'error': weather_info['error']}, 400

    # If retrieval was successful, return weather information
    return weather_info, 200
