from decimal import Decimal
from django.shortcuts import get_object_or_404
from plants.models import Plant


def basket_contents(request):
    """
    Context to hold basket contents
    basket_contents code supplied by Code Institute
    """
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        plant = get_object_or_404(Plant, pk=item_id)
        total += item_data * plant.price
        plant_count += item_data
        basket_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'plant': plant,
        })

    vat = 23 * total

    grand_total = total + vat

    context = {
        'basket_items': basket_items,
        'total': total,
        'plant_count': product_count,
        'vat': vat,
        'grand_total': grand_total,
    }

    return context
