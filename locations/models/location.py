from django.db import models


class Location(models.Model):
    """
    A model representing a location.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Return the string representation of the location.
        """
        return self.name
