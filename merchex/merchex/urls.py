"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='groupe-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:id>/change/', views.band_change,name='band-change'),
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'),
    path('about-us/', views.about),
    path('listings/', views.listings, name='listing-list'),
    path('listings/<int:id>/', views.listings_detail, name='list-detail'),
    path('listings/add/', views.listings_create, name='list-create'),
    path('listings/<int:id>/change/', views.listing_update, name='listing-update'),
    path('listings/<int:id>/delete', views.listing_delete, name='listing-delete'),
    path('contact-us/', views.contact, name='contact'),
    path('email-sent/', views.emailsent, name='email-sent'),
]
