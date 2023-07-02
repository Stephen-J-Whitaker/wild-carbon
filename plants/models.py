from django.db import models


class Plant(models.Model):
    """
    Model class to hold plant instances
    """
    common_name = models.CharField(max_length=150)
    genus = models.CharField(max_length=150)
    species = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        """
        Override __str__ with the plant common name
        """
        return self.common_name

    class Meta:
        """
        Ensure a system can't have duplciate plant common names
        """
        constraints = [
            models.UniqueConstraint(fields=['common_name'],
                                    name='unique_common_name'),
            models.UniqueConstraint(fields=['sku'],
                                    name='unique_sku_name')
        ]


class PlantState(models.Model):
    """
    Model class to hold the possible plant states
    """
    plant_state_name = models.CharField(max_length=90, unique=True)
    plant_state_friendly_name = models.CharField(max_length=90)
    next_plant_state = models.ForeignKey('self', on_delete=models.SET_NULL,
                                         null=True, blank=True,
                                         related_name='plant_states')

    def __str__(self):
        """
        Override __str__ with the state friendly name
        """
        return self.plant_state_friendly_name


class PlantRecord(models.Model):
    """
    Model class to hold plant records
    """
    from checkout.models import Order  # Prevent circular imports
    from locations.models import Location  # Prevent circular imports
    plant = models.ForeignKey(Plant, on_delete=models.SET_NULL, null=True,
                              blank=False, related_name='plant_records')
    plant_number = models.IntegerField(null=True, blank=True)
    date_state_changed = models.DateField(auto_now=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,
                              blank=True, related_name='order_plant_records')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,
                                 null=True, blank=False,
                                 related_name='location_plant_records')
    plant_state = models.ForeignKey(PlantState, on_delete=models.SET_NULL,
                                    null=True, blank=False,
                                    related_name='plant_state_plant_records')

    class Meta:
        """
        Ensure the system can't have duplicate plant ids
        """
        constraints = [
            models.UniqueConstraint(fields=['plant_id'],
                                    name='unique_plant_id'),
        ]

    def __str__(self):
        """
        Override __str__ with the plant common name
        """
        return self.plant.common_name
