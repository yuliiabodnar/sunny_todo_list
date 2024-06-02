from django.http import JsonResponse
from django.views import View
from tasks.models.task import Task
from locations.models.location import Location


class TaskListAPIView(View):
    def get(self, request):
        # Get the list of Location objects associated with tasks
        locations = Location.objects.filter(task__isnull=False).distinct()

        locations_context = []
        for location in locations:
            location_weather_info = location.get_weather_info(request)
            locations_context.append(location_weather_info)

        return JsonResponse(locations_context, safe=False)
