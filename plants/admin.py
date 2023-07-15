from django.contrib import admin
from .models import Plant, PlantRecord


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
    search_fields = ['genus', 'species', 'common_name']


admin.site.register(Plant, PlantAdmin)


@admin.register(PlantRecord)
class PlantRecord(admin.ModelAdmin):
    """
    Plant Record admin registration class
    """
    list_display = ('plant', 'plant_number', 'order', 'plant_state',
                    'date_state_changed')
    search_fields = ['order', 'plant']
