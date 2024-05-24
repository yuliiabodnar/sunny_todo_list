from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('get/', views.get, name='get'),
]