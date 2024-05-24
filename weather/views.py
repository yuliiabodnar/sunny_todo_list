from django.http import JsonResponse
from django.shortcuts import render


def get(request):
    location_info = {
        'location': 'London'
    }

    return JsonResponse(location_info)