from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages

from plants.models import Plant


def view_basket(request):
    """
    A view that renders the bag contents page
    view_basket code supplied by Code Institute
    """
    return render(request, 'basket/view_basket.html')
