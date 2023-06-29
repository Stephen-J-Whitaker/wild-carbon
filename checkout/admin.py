from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    A class to show the order line items in
    the admin page
    OrderLineItemAdminInline class provided by Code Institute
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    A class to add orders to the admin page
    OrderAdmin class provided by Code Institute
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'vat', 'order_total',
                       'grand_total', 'original_basket',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'vat',
              'order_total', 'grand_total', 'original_basket',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'vat',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
