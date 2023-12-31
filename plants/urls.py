from django.urls import path
from . import views

urlpatterns = [
     path('list_plants/', views.all_plants, name='list_plants'),
     path('add_plant/', views.add_plant, name='add_plant'),
     path('edit_plant/<int:plant_id>/', views.edit_plant, name='edit_plant'),
     path('plant_detail/<int:location_id>/<int:pk>/',
          views.PlantDetail.as_view(),
          name='plant_detail'),
     path('delete_plant/<int:pk>',
          views.DeletePlant.as_view(), name='delete_plant'),
     path('common_name_validate/', views.common_name_validate,
          name='common_name_validate'),
     path('list_plant_records/', views.list_plant_records,
          name='list_plant_records'),
     path('change_plant_state/<int:record_pk>', views.change_plant_state,
          name='change_plant_state'),
     path('add_plant_record/', views.AddPlantRecord.as_view(),
          name='add_plant_record'),
     path('delete_plant_record/<int:pk>',
          views.DeletePlantRecord.as_view(),
          name='delete_plant_record'),
]
