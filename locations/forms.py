from .models import Location
from plants.models import Plant
from django import forms


class LocationPlantsForm(forms.ModelForm):
    """
    Form class for associating a location
    with a group of plants
    """
    class Meta:
        model = Location
        fields = ('location_plants',)
    location_plants = forms.ModelMultipleChoiceField(
        queryset=Plant.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
