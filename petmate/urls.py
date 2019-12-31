"""petmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import petlisting.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', petlisting.views.index, name='index'),
    path('petdetails/', petlisting.views.petdetails, name='petdetails'),
    path('petpreview/', petlisting.views.petpreview, name='petpreview'),
    path('petlisting/', petlisting.views.petlisting, name='petlisting'),
    # path('', TemplateView.as_view(template_name=') index, name='index'),
    # path('petdetails', TemplateView.as_view(template_name='petdetails.html'), name='petdetails'),
    # path('petpreview', TemplateView.as_view(template_name='petpreview.html'), name='petpreview')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)