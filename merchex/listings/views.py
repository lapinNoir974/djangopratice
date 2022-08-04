from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def band_list(request):
	bands = Band.objects.all()
	return render(request, 'listings/band_list.html',
					context={"bands" : bands})

def band_detail(request, id):
	return render(request,
			'listings/band_detail.html',
			{'id': id})

def about(request):
	return render(request, 'listings/about.html')

def listings(request):
	listings = Listing.objects.all()
	return render(request, 'listings/list.html',
					context={"listings" : listings})

def contact(request):
	return render(request, 'listings/contact.html')