from django.db import models
from locations.models import Location  # Import the Location model


class TaskManager(models.Manager):
    """
    A custom manager for the Task model.
    """
    def get_all_locations(self):
        """
        Retrieve all unique location names associated with tasks.

        Returns:
            list: A list of unique location names.
        """
        # Retrieve all Task objects
        tasks = self.all()

        # Initialize an empty list to store cities
        location_names = []

        # Iterate over each Task object
        for task in tasks:
            # Retrieve the related Location object for the task
            location = task.location

            # If location exists, append its name to the list
            if location:
                location_names.append(location.name)

        # Remove duplicates from the list of cities
        unique = list(set(location_names))

        return unique


class Task(models.Model):
    """
    A model representing a task.
    """
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
