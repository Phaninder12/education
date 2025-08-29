from django import forms
from educationapp.models import Parent
from educationapp.models import Contact



class ParentForm(forms.ModelForm):
	class Meta:
		model = Parent
		fields = '__all__'

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
