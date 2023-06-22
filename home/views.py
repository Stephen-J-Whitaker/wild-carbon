from django.shortcuts import render


def index(request):
    """
    A view to render the landing page
    """
    return render(request, 'home/index.html')
