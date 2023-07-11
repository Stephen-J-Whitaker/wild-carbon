from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm
import profiles.co2_calculations as co2_calculations
from django.conf import settings


@login_required
def profile(request):
    """
    Display the user's profile
    profile view code supplied by Code Institute
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please'
                           ' ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all().order_by('date')
    order_data = []
    for order in orders:
        order_record_data = {}
        order_records = (order.order_plant_records.all().
                         order_by('-plant_state', 'plant'))
        order_record_data['order'] = order
        order_record_data['plant_records'] = order_records
        order_data.append(order_record_data)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'order_data': order_data,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display the details of a historic user order as selected
    order_history code supplied by Code Institute
    """
    order = get_object_or_404(Order, order_number=order_number)

    if request.user != order.user_profile.user:
        messages.success(request, 'Sorry, you dont have permission'
                         'to look at this order')
        return redirect(reverse('home'))

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def record_sort_pending(all_records):
    """
    Filter for pending records
    """
    pending = (all_records.
               filter(plant_state__plant_state_name__contains='pending'))
    return pending


def record_sort_growing(all_records):
    """
    Filter for growing records
    """
    growing = (all_records.
               filter(plant_state__plant_state_name__contains='growing'))
    return growing


def record_sort_planted(all_records):
    """
    Filter for planted records
    """
    planted = (all_records.
               filter(plant_state__plant_state_name__contains='planted'))
    return planted


@login_required
def carbon_summary(request):
    """
    Display the user's carbon summary
    """

    if request.method == 'GET':

        all_user_orders = []
        pending = []
        growing = []
        planted = []
        plant_count = co2_calculations.user_plants(request)
        sequestered_co2 = co2_calculations.sequestered_co2(plant_count)
        co2_outstanding = co2_calculations.co2_outstanding(sequestered_co2)
        plants_outstanding = (co2_calculations.
                              plants_outstanding(co2_outstanding))
        tree_life = settings.TREE_LIFE_EXPECTANCY

        profile = get_object_or_404(UserProfile, user=request.user)
        all_user_orders = profile.orders.all()
        first_pass = True

        for order in all_user_orders:
            all_records = (order.order_plant_records.all())
            if first_pass:
                pending = record_sort_pending(all_records)
                growing = record_sort_growing(all_records)
                planted = record_sort_planted(all_records)
                first_pass = False
            pending = (pending.union(record_sort_pending(all_records)).
                       order_by('plant', 'date_state_changed'))
            growing = (growing.union(record_sort_growing(all_records)).
                       order_by('plant', 'date_state_changed'))
            planted = (planted.union(record_sort_planted(all_records)).
                       order_by('plant', 'date_state_changed'))

    template = 'profiles/carbon_summary.html'
    context = {
        'all_user_orders': all_user_orders,
        'plant_count': plant_count,
        'tree_life': tree_life,
        'sequestered_co2': sequestered_co2,
        'co2_outstanding': co2_outstanding,
        'plants_outstanding': plants_outstanding,
        'pending': pending,
        'growing': growing,
        'planted': planted,
    }

    return render(request, template, context)
