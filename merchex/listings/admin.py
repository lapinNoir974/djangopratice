from django.contrib import admin

# Register your models here.

from listings.models import Band

class BandAdmin(admin.ModelAdmin):
	list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste


admin.site.register(Band, BandAdmin)

from listings.models import Listing

class ListingAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'sold','band')

admin.site.register(Listing, ListingAdmin)