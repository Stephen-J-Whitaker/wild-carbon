# Module for carbon summary calculations

from django.shortcuts import get_object_or_404
from django.db.models import Sum
from profiles.models import UserProfile


def user_trees(request):
    """
    Return the total number of trees commissioned by the user
    """
    print('in trees planted')
    profile = get_object_or_404(UserProfile, user=request.user)
    user_orders = profile.orders.all()
    print(user_orders)
    plant_count = 0
    for order in user_orders:
        line_items = order.lineitems.all()
        for line_item in line_items:
            plant_count += line_item.quantity
            print(plant_count)
    return plant_count
