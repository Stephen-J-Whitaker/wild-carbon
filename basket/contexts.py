from decimal import Decimal
from django.shortcuts import get_object_or_404
from locations.models import Location
from django.conf import settings


def basket_contents(request):
    """
    Context to hold basket contents
    basket_contents code supplied by Code Institute
    """
    basket_items = []
    total = 0
    plant_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        get_object_or_404(Location, pk=1)
        location_plants = (Location.objects.get(pk=1).
                           location_plants.all())
        plant = get_object_or_404(location_plants, pk=item_id)

        total += item_data * plant.price
        plant_count += item_data
        basket_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'plant': plant,
        })

    vat = total * Decimal(settings.VAT / 100)

    grand_total = total + vat

    context = {
        'basket_items': basket_items,
        'total': total,
        'plant_count': plant_count,
        'vat': vat,
        'grand_total': grand_total,
    }

    return context
