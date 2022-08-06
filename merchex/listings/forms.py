from django import forms
from listings.models import Band, Listing
class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
   class Meta:
      model = Band
      #ON desactive tous les champs dispo du formulaire
      #fields ='__all__'
      #On exclu les champs qu'on veut pas que l'utilisateur utilise
      exclude = ('active', 'official_homepage') 

class ListForm(forms.ModelForm):
   class Meta:
      model = Listing
      fields ='__all__'