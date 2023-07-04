from locations.models import Location, Plant
from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.shortcuts import get_object_or_404
import copy


def clean_basket(request):
    """
    Remove non existent items from basket
    """
    basket = request.session.get('basket', {})
    clean_basket = copy.deepcopy(basket)
    basket_clean = True
    if basket != {}:
        for item_id, item_data in basket.items():
            get_object_or_404(Location, pk=1)
            location_plants = (Location.objects.get(pk=1).
                               location_plants.all())
            print('location plants', location_plants)
            if not location_plants.filter(id=item_id).exists():
                print('not at location', item_id)
                clean_basket.pop(item_id)
                print('clean_basket', clean_basket)
                basket_clean = False
        print(clean_basket)
        request.session['basket'] = clean_basket
        if not basket_clean:
            messages.error(request, (
                        "Sorry, one or more of the plants "
                        " in your basket is no longer "
                        "available and has removed")
                    )
            return redirect(reverse('view_basket'))
        else:
            return True
    else:
        return True
