from django.urls import path
from . import views

urlpatterns = [
    path('view_basket/', views.view_basket, name='view_basket'),
    path('add_to_basket/<item_id>/', views.add_to_basket,
         name='add_to_basket'),
    path('adjust_basket/<item_id>/', views.adjust_basket,
         name='adjust_basket'),
    path('remove_from_basket/<item_id>/', views.remove_from_basket,
         name='remove_from_basket'),
]
