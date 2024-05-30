from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from locations.models.location import Location



class TaskLocationAPIView(View):

    def get_location(self, location_id):
        if location_id:
            return get_object_or_404(Location, pk=location_id)
        return None

    def get(self, request, pk=None):

        location = self.get_location(pk)

        location_context = []
        if location:
            location_weather_info = location.get_weather_info(request)
            location_context.append(location_weather_info)

        return JsonResponse(location_context, safe=False)
