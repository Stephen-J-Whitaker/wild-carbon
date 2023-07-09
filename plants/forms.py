from django import forms
from .widgets import CustomClearableFileInput
from .models import Plant, PlantRecord


class PlantForm(forms.ModelForm):
    """
    Form class for adding plants
    AddPlantForm class code supplied by Code Institute
    """
    class Meta:
        model = Plant
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)


class AddPlantRecordForm(forms.ModelForm):
    """
    Form class for adding plant records
    """
    class Meta:
        model = PlantRecord
        fields = ('plant',)

    plant = forms.ModelChoiceField(queryset=Plant.objects.all(),
                                   empty_label='Select a plant')
