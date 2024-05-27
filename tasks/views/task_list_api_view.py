from django.http import JsonResponse
from django.views import View
from ..models.task import Task
from ..weather.weather_service import WeatherService
from ..weather.weather_parser import WeatherParser


class TaskListAPIView(View):
    def get(self, request):
        weather_service = WeatherService(request)
        weather_parser = WeatherParser()

        # Get the list of locations from the Task model
        locations = Task.objects.values_list('location__name', flat=True).distinct()

        location_context = []
        for location in locations:
            location_weather_info = weather_service.get_weather_info(location)
            parsed_weather_info = weather_parser.parse_location_weather_response(location, location_weather_info)
            location_context.append(parsed_weather_info)

        return JsonResponse(location_context, safe=False)
