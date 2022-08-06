from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListForm
from django.core.mail import send_mail
from django.shortcuts import redirect

def band_list(request):
	bands = Band.objects.all()
	return render(request, 'listings/band_list.html',
					context={"bands" : bands})

def band_detail(request, id):
	band = Band.objects.get(id=id)
	return render(request,
			'listings/band_detail.html',
			{'band': band})

def band_create(request):
	if request.method =='POST':
		form = BandForm(request.POST)
		if form.is_valid():
			#creer une nouvelle 'band' et la sauvegarde dans le BDD
			band = form.save()
			# Redirige vers la page de details du groupe que venons de creer
			#nous pouvons fournir les arugment du motif URL comme arguments à la fonction de redirection
			return redirect('band-detail', band.id)
	else:
		form = BandForm()
	
	return render(request,
		'listings/bandcreation.html',
		{'form': form})

def band_change(request, id):
	band = Band.objects.get(id=id)
	
	if request.method =='POST':
		form = BandForm(request.POST, instance=band)
		if form.is_valid():
		#MAJ du group existant dans la BDD
			form.save()
		#redirige vers la page du groupe de la MAJ
			return redirect('groupe-detail', band.id)
	else:
		form = BandForm(instance=band)

	return render(request,
		'listings/band_update.html',
		{'form': form})

def about(request):
	return render(request, 'listings/about.html')

def listings(request):
	listings = Listing.objects.all()
	return render(request, 'listings/list.html',
					context={"listings" : listings})

def listings_detail(request, id):
	listing = Listing.objects.get(id=id)
	return render(request,
		'listings/listings_detail.html',
		{'listing': listing})

def listings_create(request):
	if request.method =='POST':
		form = ListForm(request.POST)
		if form.is_valid():
			listi = form.save()
			return redirect('list-detail', listi.id)
	else:
		form = ListForm()

	return render(request,
	 	'listings/listing_creation.html',
		{'form' :form})

def listing_update(request, id):
	listing = Listing.objects.get(id=id)

	if request.method =='POST':
		form = ListForm(request.POST,instance=listing)
		if form.is_valid():
			form.save()
			return redirect('list-detail', listing.id)
	else:
		form = ListForm(instance=listing)
		
	return render(request,
			'listings/listing_update.html',
			{'form': form})


def contact(request):
	#on creer une instruction if pour les methode post ou get
	if request.method == 'POST':
		#creer une instance de notre formulaire et le remplir avec les donnes POST
		form = ContactUsForm(request.POST)

		if form.is_valid():
			send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
		return redirect('email-sent') #instruction de retour du formulaire
	else:
		#ceci doit être une requete GET, donc creer un formulaire vide
		form = ContactUsForm()
	return render(request,
			'listings/contact.html',
			{'form': form}) # passe ce formulaire au gabarit

def emailsent(request):
	return render(request, 'listings/confirmation.html')