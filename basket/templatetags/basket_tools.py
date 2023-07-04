from django import template
from django.conf import settings
from decimal import Decimal


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate the basket subtotal
    cal_subtotal code supplied by Code Institute
    """
    return price * quantity


@register.filter(name='calc_vat')
def calc_vat(price):
    """
    Calculate the vat of a product
    """
    plant_vat = price * Decimal(settings.VAT / 100)
    return plant_vat + price
