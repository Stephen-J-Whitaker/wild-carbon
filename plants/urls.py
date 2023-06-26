from django.urls import path
from . import views

urlpatterns = [
    path('plant_list/', views.all_plants, name='plant_list'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('edit_plant/<int:plant_id>/', views.edit_plant, name='edit_plant'),
    path('plant_delete/<int:pk>',
         views.PlantDelete.as_view(), name='plant_delete'),
    path('common_name_validate/', views.common_name_validate,
         name='common_name_validate'),
]
