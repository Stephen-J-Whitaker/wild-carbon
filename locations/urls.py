from django.urls import path
from . import views

urlpatterns = [
    path('location_plants_link/<int:pk>', views.LocationsPlants.as_view(),
         name='location_plants_link'),
    path('carbon_capture/', views.location_plants, name='carbon_capture'),
]
