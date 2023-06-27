from django import forms
from .widgets import CustomClearableFileInput
from .models import Plant


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