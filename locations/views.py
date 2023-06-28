from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View, generic
from .forms import LocationPlantsForm
from .models import Location
from django.db.models.functions import Lower
from django.db.models import Q
from django.contrib import messages


class LocationsPlants(LoginRequiredMixin, UserPassesTestMixin,
                      generic.UpdateView):
    """
    A class based view to associate plants with a location
    """
    model = Location
    form_class = LocationPlantsForm
    template_name = 'locations/location_plants_link.html'
    success_url = '/carbon_capture'

    def test_func(self):
        if not self.request.user.is_superuser:
            messages.error(self.request, 'Sorry, only Wild Carbon '
                           'staff can do that.')
        return self.request.user.is_superuser


def location_plants(request):
    """
    A view to show all the plants associated with a
    location, including sort and search queries
    location_plants view code supplied by Code Institute
    """
    plants = Location.objects.get(pk=1).location_plants.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'common_name':
                sortkey = 'lower_common_name'
                plants = plants.annotate(lower_common_name=Lower
                                         ('common_name'))
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
                return redirect(reverse('carbon_capture'))

            queries = (Q(common_name__icontains=query) |
                       Q(genus__icontains=query) |
                       Q(species__icontains=query) |
                       Q(description__icontains=query))

            plants = plants.filter(queries)

    current_sorting = f'{sort}__{direction}'

    location_name = get_object_or_404(Location, pk=1).location_friendly_name
  
    context = {
        'plants': plants,
        'search_term': query,
        'current_sorting': current_sorting,
        'location_name': location_name,
    }

    return render(request, 'locations/carbon_capture.html', context)
