from django.http import JsonResponse
from .services.weather_info_service import get_weather_info


def get(request):
    # Get the API key from the request object
    api_key = request.api_key

    # Get location from the request query parameters
    location = request.GET.get('location')

    # Retrieve weather information for the specified location
    weather_info, status_code = get_weather_info(location, api_key)

    # Return the weather information or error response
    return JsonResponse(weather_info, status=status_code)
