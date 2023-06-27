from django.urls import path
from . import views

urlpatterns = [
    path('list_plants/', views.all_plants, name='list_plants'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('edit_plant/<int:plant_id>/', views.edit_plant, name='edit_plant'),
    path('delete_plant/<int:pk>',
         views.DeletePlant.as_view(), name='delete_plant'),
    path('common_name_validate/', views.common_name_validate,
         name='common_name_validate'),
]
