from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q

from .models import Plant
from .forms import AddPlantForm


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


@login_required
def add_plant(request):
    """
    Add a plant instance to the database
    add_plant view code supplied by Code Institute
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Wild Carbon '
                       'staff can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AddPlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save()
            messages.success(request, 'Successfully added plant!')
            return redirect(reverse('plant_list'))
        else:
            messages.error(request, 'Failed to add plant.'
                           'Please ensure the form is valid.')
    else:
        form = AddPlantForm()

    template = 'plants/add_plant.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
