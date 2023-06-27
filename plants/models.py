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
