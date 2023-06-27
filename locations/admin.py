from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """
    Location admin registration class
    """
    list_display = (
        'location_friendly_name',
        'location_name'
    )
