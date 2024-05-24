from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('tasks.urls', 'tasks'), namespace='tasks')),
    path('weather/', include(('weather.urls', 'weather'), namespace='weather')),
]
