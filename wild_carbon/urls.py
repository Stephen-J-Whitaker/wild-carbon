"""wild_carbon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls'), name='home_urls'),
    path('', include('plants.urls'), name='plants_urls'),
    path('', include('locations.urls'), name='locations_urls'),
    path('', include('basket.urls'), name='basket_urls'),
    path('checkout/', include('checkout.urls')),
    # Code to serve robots.txt sourced at:
    # https://ngangasn.com/sitemap-robot-txt-django/?expand_article=1
    path('robots.txt', TemplateView.as_view(template_name='robots.txt',
                                            content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml',
                                             content_type='text/xml')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
