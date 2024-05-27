from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from ..models.location import Location
from ..weather.weather_service import WeatherService
from ..weather.weather_parser import WeatherParser


class TaskLocationAPIView(View):

    def get_location(self, location_id):
        if location_id:
            return get_object_or_404(Location, pk=location_id)
        return None

    def get(self, request, pk=None):
        weather_service = WeatherService(request)
        weather_parser = WeatherParser()

        location = self.get_location(pk)

        location_context = []

        if location:
            location_weather_info = weather_service.get_weather_info(location.name)
            parsed_weather_info = weather_parser.parse_location_weather_response(location.name, location_weather_info)
            location_context.append(parsed_weather_info)

        return JsonResponse(location_context, safe=False)