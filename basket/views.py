from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages

from plants.models import Plant
from locations.models import Location


def view_basket(request):
    """
    A view that renders the bag contents page
    view_basket code supplied by Code Institute
    """
    return render(request, 'basket/view_basket.html')


def add_to_basket(request, item_id):
    """
    Add a quantity of the specified plant to the basket
    add_to_basket code supplied by Code Institute
    """
    get_object_or_404(Location, pk=1)
    location_plants = (Location.objects.get(pk=1).
                       location_plants.all())
    plant = get_object_or_404(location_plants, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        name = plant.common_name
        messages.success(request,
                         f'Updated {name} quantity to {basket[item_id]}',
                         extra_tags='show-basket')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {plant.common_name} to your basket',
                         extra_tags='show-basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust the quantity of the specified product
    to the specified amount
    adjust_basket code supplied by Code Institute
    """

    get_object_or_404(Location, pk=1)
    location_plants = (Location.objects.get(pk=1).
                       location_plants.all())
    plant = get_object_or_404(location_plants, pk=item_id)

    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, (f'Updated {plant.common_name} '
                                   f'quantity to {basket[item_id]}'
                                   ), extra_tags='show-basket')
    else:
        basket.pop(item_id)
        messages.success(request,
                         f'Removed {plant.common_name} from your basket',
                         extra_tags='show-basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    Remove the item from the shopping bag
    remove_from_basket code supplied by Code Institute
    """

    try:
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(request, f'Removed plant '
                         f'from your basket',
                         extra_tags='show-basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
