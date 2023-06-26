from django.shortcuts import render
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q

from .models import Plant


def all_plants(request):
    """
    A view to show all the plant instances
    including sort and search queries

    all_plants view code supplied by Code Institute
    """
    plants = Plant.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'common_name':
                sortkey = 'lower_common_name'
                plants = plants.annotate(lower_name=Lower('common_name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            plants = plants.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('plants'))

            queries = ('Q(name__icontains=query) | '
                       'Q(description__icontains=query)')
            plants = plants.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'plants': plants,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'plants/plant_list.html', context)
