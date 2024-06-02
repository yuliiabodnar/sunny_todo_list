from django.http import JsonResponse
from django.views import View
from tasks.models.task import Task
from locations.models.location import Location
from tasks.handlers.views.context_handler import get_locations_context


class TaskListAPIView(View):
    def get(self, request):
        # Get the list of Location objects associated with tasks
        locations = Location.objects.filter(task__isnull=False).distinct()
        locations_context = get_locations_context(request, locations)

        return JsonResponse(locations_context, safe=False)
