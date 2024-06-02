from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from locations.models.location import Location
from tasks.handlers.views.context_handler import get_locations_context


class TaskLocationContext(View):
    def get_location(self, location_id):
        if location_id:
            return get_object_or_404(Location, pk=location_id)
        return None

    def get(self, request, pk=None):

        location = self.get_location(pk)
        locations_context = get_locations_context(request, [location])

        return JsonResponse(locations_context, safe=False)
