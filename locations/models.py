from django.db import models
from django.urls import reverse
from plants.models import Plant


class Location(models.Model):
    """
    Model class to hold locations
    """
    location_name = models.CharField(max_length=150)
    location_friendly_name = models.CharField(max_length=150)
    location_plants = models.ManyToManyField(Plant,
                                             related_name="location_plants")

    class Meta:
        """
        Ensure the system can't have duplicate location names
        """
        constraints = [
            models.UniqueConstraint(fields=['location_name'],
                                    name='unique_location_name'),
            models.UniqueConstraint(fields=['location_friendly_name'],
                                    name='unique_location_friendly_name')
        ]

    def __str__(self):
        """
        Override __str__ with the correct location name
        """
        return self.location_name

    def get_absolute_url(self):
        """
        Provide a default success url reverse lookup
        for generic views
        """
        return reverse('home')
