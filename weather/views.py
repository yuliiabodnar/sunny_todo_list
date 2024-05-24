from django.http import JsonResponse
from .services.weather_api_service import WeatherAPIService


def get(request):
    # Get the API key from the request object
    api_key = request.api_key

    # Get location from the request query parameters
    location = request.GET.get('location')
    if not location:
        # Return error response if location parameter is missing
        return JsonResponse({'error': 'Location parameter is missing'},  status=400)

    # Get weather information for the specified location
    weather_api_service = WeatherAPIService(api_key)
    weather_info = weather_api_service.get_weather_data(location)

    # Check for any errors in weather data retrieval
    if 'error' in weather_info:
        return JsonResponse(weather_info, status=400)

    # Return weather information if retrieval was successful
    return JsonResponse(weather_info, status=200)
