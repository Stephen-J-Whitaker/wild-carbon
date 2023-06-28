from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate the basket subtotal
    cal_subtotal code supplied by Code Institute
    """
    return price * quantity
