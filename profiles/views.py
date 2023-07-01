from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
import profiles.carbon_calculations as carbon_calculations

from checkout.models import Order


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
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
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


@login_required
def carbon_summary(request):
    """
    Display the user's carbon summary
    """

    if request.method == 'GET':

        user = request.user
        print(carbon_summary)
        plant_count = carbon_calculations.user_trees(request)
        print('in carbon summary', plant_count)
      
    return render(request, 'profiles/carbon_summary.html')
