from django.shortcuts import render


def index(request):
    """
    A view to render the landing page
    index code provided by Code Institute
    """
    return render(request, 'home/index.html')


def about_us(request):
    """
    A view to render the about us page
    """
    return render(request, 'home/about_us.html')


def how_it_works(request):
    """
    A view to render the how it works page
    """
    return render(request, 'home/how_it_works.html')
