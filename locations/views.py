from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from .forms import LocationPlantsForm
from .models import Location


class LocationsPlants(generic.UpdateView):
    """
    A class based view to associate plants with a location
    """
    model = Location
    form_class = LocationPlantsForm
    template_name = 'locations/location_plants_link.html'


def index(request):
    """
    A view to render the carbon capture page
    """
    return render(request, 'locations/carbon_capture.html')
