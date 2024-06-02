from django.db import models
from locations.models import Location  # Import the Location model


class Task(models.Model):
    """
    A model representing a task.
    """
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    temperature = models.CharField(max_length=10, default='')
    is_rain = models.BooleanField(default=False)
    is_cloudy = models.BooleanField(default=False)
    is_sunny = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return the string representation of the location.
        """
        return self.name

    class Meta:
        app_label = 'tasks'