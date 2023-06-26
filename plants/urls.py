from django.urls import path
from . import views

urlpatterns = [
    path('plant_list/', views.all_plants, name='plant_list'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('common_name_validate/', views.common_name_validate,
         name='common_name_validate'),
]
