from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('tasks.urls', 'tasks'), namespace='tasks')),
    path('location/', include(('locations.urls', 'locations'), namespace='locations')),
    path('weather/', include(('weather.urls', 'weather'), namespace='weather')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)