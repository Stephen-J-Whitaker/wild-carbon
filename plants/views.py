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

from .models import Plant
from .forms import PlantForm


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
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save()
            messages.success(request, 'Successfully added plant!')
            return redirect(reverse('plant_list'))
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
            return redirect(reverse('plant_list'))
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


class PlantDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    """
    A class based view to confirm a deletion of a plant
    Code adapted from music aid project:
    https://github.com/Stephen-J-Whitaker/
        music-aid/blob/main/songbook/views.py
    """
    model = Plant
    template_name = 'plants/plant_confirm_delete.html'
    success_message = "The plant has been deleted"

    def get_context_data(self, **kwargs):
        """
        Add contexts
        """
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['plant_pk'] = self.kwargs.get('plant_pk', None)
        return context

        # Code sourced from stackoverflow.com:
        # questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PlantDelete, self).delete(request, *args, **kwargs)
        # End of code sourced from stackoverflow
        # questions/24822509/success-message-in-deleteview-not-shown

    def get_success_url(self, **kwargs):
        """
        If success send back to correct view
        """
        return reverse_lazy('plant_list')


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
