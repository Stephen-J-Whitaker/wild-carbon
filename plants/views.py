from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from wild_carbon.mixins import SuperUserRequiredMixin
from django.http import Http404

from .models import Plant, PlantRecord, PlantState
from locations.models import Location
from .forms import PlantForm, AddPlantRecordForm


def all_plants(request):
    """
    A view to show all the plant instances
    including sort and search queries

    all_plants view code supplied by Code Institute
    """
    plants = Plant.objects.all().order_by('common_name')
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
                return redirect(reverse('list_plants'))

            queries = (Q(common_name__icontains=query) |
                       Q(genus__icontains=query) |
                       Q(species__icontains=query) |
                       Q(description__icontains=query))

            plants = plants.filter(queries)

    current_sorting = f'{sort}__{direction}'

    context = {
        'plants': plants,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'plants/list_plants.html', context)


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
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save()
            messages.success(request, 'Successfully added plant!')
            return redirect(reverse('list_plants'))
        else:
            messages.error(request, 'Failed to add plant.'
                           'Please ensure the form is valid.')
    else:
        form = PlantForm()

    template = 'plants/add_plant.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_plant(request, plant_id):
    """
    Edit a product in the system
    edit_plant view code supplied by Code Institute
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Wild Carbon staff can do that.')
        return redirect(reverse('home'))

    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated plant!')
            return redirect(reverse('list_plants'))
        else:
            messages.error(request, 'Failed to update plant. '
                           'Please ensure the form is valid.')
    else:
        form = PlantForm(instance=plant)
        messages.info(request, f'You are editing {plant.common_name}')

    template = 'plants/edit_plant.html'
    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, template, context)


class DeletePlant(SuperUserRequiredMixin, SuccessMessageMixin,
                  generic.DeleteView):
    """
    A class based view to confirm a deletion of a plant
    Code adapted from music aid project:
    https://github.com/Stephen-J-Whitaker/
        music-aid/blob/main/songbook/views.py
    """
    model = Plant
    template_name = 'plants/confirm_delete_plant.html'
    success_message = 'The plant has been deleted'

    # Code sourced from stackoverflow.com:
    # questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        plant_id = self.kwargs['pk']
        plant = get_object_or_404(Plant, pk=plant_id)
        plant.image.delete()
        messages.success(self.request, self.success_message)
        return super(DeletePlant, self).delete(request, *args, **kwargs)
        # End of code sourced from stackoverflow
        # questions/24822509/success-message-in-deleteview-not-shown

    def get_success_url(self, **kwargs):
        """
        If success send back to correct view
        """
        return reverse_lazy('list_plants')


class PlantDetail(generic.DetailView):
    """
    Class based view to view plant details
    """
    model = Plant
    template_name = 'plants/plant_detail.html'

    def get_queryset(self):
        """
        Define the queryset to be used and confirm the plant is
        available at the location
        """
        location_id = self.kwargs['location_id']
        get_object_or_404(Location, pk=location_id)
        location_plants = (Location.objects.get(pk=location_id).
                           location_plants.all())
        get_object_or_404(location_plants, pk=self.kwargs['pk'])

        return super().get_queryset()


def common_name_validate(request):
    """
    Verify the common name is unique in the system
    Code taken from music aid project:
    https://github.com/Stephen-J-Whitaker/music-aid/blob/
        main/static/js/songbook_js/songbook_song_add_edit.js
    """
    if request.method == 'GET':
        common_name = request.GET['common_name']
        if Plant.objects.filter(common_name__iexact=common_name).exists():
            return HttpResponse("in_use")
        else:
            return HttpResponse("available")


@login_required
def list_plant_records(request):
    """
    List all of the plant records
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Wild Carbon '
                       'staff can do that.')
        return redirect(reverse('home'))

    if request.method == 'GET':
        all_records = PlantRecord.objects.all()

        pending = ((all_records.
                   filter(plant_state__plant_state_name__contains='pending')).
                   order_by('date_state_changed', 'plant'))
        growing = ((all_records.
                   filter(plant_state__plant_state_name__contains='growing')).
                   order_by('date_state_changed', 'plant'))
        planted = ((all_records.
                   filter(plant_state__plant_state_name__contains='planted')).
                   order_by('date_state_changed', 'plant'))
    template = 'plants/list_plant_records.html'
    context = {
        'pending': pending,
        'growing': growing,
        'planted': planted,
    }

    return render(request, template, context)


@login_required
def change_plant_state(request, record_pk):
    """
    Change the plant state in the plant record
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Wild Carbon '
                       'staff can do that.')
        return redirect(reverse('home'))

    record = get_object_or_404(PlantRecord, pk=record_pk)
    if request.method == 'GET':
        if record.plant_state.plant_state_name == 'planted':
            messages.error(request, 'Sorry, thant plant is planted'
                           ' which is the last state')
            return redirect(reverse('list_plant_records'))

        template = 'plants/change_plant_state.html'
        context = {
            'record': record,
        }
        return render(request, template, context)

    if request.method == 'POST':
        if record.plant_state.plant_state_name == 'planted':
            messages.error(request, 'Sorry, thant plant is planted'
                           ' which is the last state')
            return redirect(reverse('list_plant_records'))
        record.plant_state = record.plant_state.next_plant_state
        record.save()
        messages.success(request, ('The state of the plant has been changed'))
        return redirect(reverse('list_plant_records'))


class AddPlantRecord(SuperUserRequiredMixin, SuccessMessageMixin,
                     generic.CreateView):
    """
    Class based iview to add a plant record
    """
    form_class = AddPlantRecordForm
    model = PlantRecord
    template_name = 'plants/add_plant_record.html'
    success_message = 'The plant record has been added'
    success_url = reverse_lazy('list_plant_records')

    def form_valid(self, form):
        """
        Add the location of the plant to the form
        """
        plant_location = Location.objects.get(location_name='west_mayo')
        form.instance.location = plant_location
        return super().form_valid(form)


class DeletePlantRecord(SuperUserRequiredMixin, SuccessMessageMixin,
                        generic.DeleteView):
    """
    A class based view to confirm a deletion of a plant record
    """
    model = PlantRecord
    template_name = 'plants/confirm_delete_plant_record.html'
    success_message = 'The plant record has been deleted'
    error_message = 'Sorry, this plant is in a state of planted'

    # Code sourced from stackoverflow.com:
    # questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        record_pk = self.kwargs['pk']
        plant_record = get_object_or_404(PlantRecord, pk=record_pk)
        print(plant_record.plant_state.plant_state_name)
        if plant_record.plant_state.plant_state_name == 'planted':
            raise Http404(self.error_message)
        messages.success(self.request, self.success_message)
        return super(DeletePlantRecord, self).delete(request, *args, **kwargs)
        # End of code sourced from stackoverflow
        # questions/24822509/success-message-in-deleteview-not-shown

    def get_success_url(self, **kwargs):
        """
        If success send back to correct view
        """
        return reverse_lazy('list_plant_records')
