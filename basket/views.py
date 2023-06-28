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
                         f'Updated {name} quantity to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {plant.common_name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)
