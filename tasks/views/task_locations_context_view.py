from django.http import JsonResponse
from django.db.models import Q
from django.views import View
from locations.models.location import Location
from tasks.handlers.views.context_handler import get_locations_context


class TaskLocationsContext(View):
    """
    Handle GET requests to retrieve a list of locations associated with not completed tasks.

    Args:
        request (HttpRequest): The HTTP GET request object.

    Returns:
        JsonResponse: A JSON response containing the context data for the locations.
    """
    def get(self, request):
        # Get the list of Location objects associated with not completed tasks
        locations = Location.objects.exclude(Q(task__isnull=True)
        ).distinct()
        locations_context = get_locations_context(request, locations)

        return JsonResponse(locations_context, safe=False)
