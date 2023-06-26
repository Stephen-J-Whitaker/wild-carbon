from django.contrib import admin
from .models import Plant


class PlantAdmin(admin.ModelAdmin):
    """
    Plant admin registration class
    """
    list_display = (
        'genus',
        'species',
        'common_name',
        'image',
        'price',
        'sku',
    )


admin.site.register(Plant, PlantAdmin)
