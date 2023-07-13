from .models import Location
from plants.models import Plant
from django import forms


class LocationPlantsForm(forms.ModelForm):
    """
    Form class for associating a location
    with a group of plants
    Code sourced at:
    https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024
    """
    class Meta:
        model = Location
        fields = ('location_plants',)
    location_plants = forms.ModelMultipleChoiceField(
        queryset=Plant.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
