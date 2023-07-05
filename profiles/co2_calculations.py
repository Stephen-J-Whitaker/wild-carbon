# Module for carbon summary calculations

from django.shortcuts import get_object_or_404
from profiles.models import UserProfile
from django.conf import settings


def user_plants(request):
    """
    Return the total number of plants commissioned by the user
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    user_orders = profile.orders.all()
    plant_count = 0
    for order in user_orders:
        line_items = order.lineitems.all()
        for line_item in line_items:
            plant_count += line_item.quantity
    return plant_count


def sequestered_co2(plant_count):
    """
    Calculate the amount of carbon these trees will
    sequester in their lifetime
    """
    sequestered_co2 = (plant_count * settings.TREE_CO2_PER_YEAR *
                       settings.TREE_LIFE_EXPECTANCY)

    return sequestered_co2


def co2_outstanding(sequestered_co2):
    """
    Calculate the amount co2 created in the users life
    that will not be offset by the platns they've
    commissioned
    """
    co2_outstanding = ((settings.HUMAN_LIFE_EXPECTANCY *
                       settings.HUMAN_ANNUAL_CARBON_FOOTPRINT) -
                       sequestered_co2)
    return co2_outstanding


def plants_outstanding(co2_outstanding):
    """
    Calculate number of additional plants
    the user must commission to offset their
    lifes carbon
    """
    plants_outstanding = round(co2_outstanding /
                               (settings.TREE_CO2_PER_YEAR *
                                settings.TREE_LIFE_EXPECTANCY))
    return plants_outstanding
