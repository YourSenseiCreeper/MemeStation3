from django import forms
from . import models

class AddMeme(forms.ModelForm):
	class Meta:
		model = models.Meme
		fields = ['description', 'image']
