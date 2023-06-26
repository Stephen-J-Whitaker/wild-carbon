from django.db import models


class Plant(models.Model):
    """
    Model class to hold plant instances
    """
    genus = models.CharField(max_length=150, blank=True)
    species = models.CharField(max_length=150, blank=True)
    common_name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=150, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        """
        Override __str__ with the plant common name
        """
        return self.common_name
