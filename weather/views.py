from django.http import JsonResponse
from .services.weather_service import WeatherService


def get(request):
    # Get location from the request query parameters
    location = request.GET.get('location')
    api_key = '3f60bb87e96c83c0f9758c61a33a590e'

    if location:
        # Initialize WeatherService with the API key
        weather_service = WeatherService(api_key)

        # Get weather information for the specified location
        weather_info = weather_service.get_weather_data(location)

        # Check for any errors in weather data retrieval
        if 'error' in weather_info:
            # Return error response if weather data retrieval failed
            return JsonResponse(
                weather_info,
                status=400
            )

        # Return weather information if retrieval was successful
        return JsonResponse(weather_info)
    else:
        # Return error response if location parameter is missing
        return JsonResponse(
            {'error': 'Location parameter is missing'},
            status=400
        )
