from django import forms
from buddyapp.models import Route

class UploadRouteForm(forms.Form):
    name = forms.CharField(max_length = 50, help_text="Name: ", required = True)
    description = forms.CharField(max_length =140, help_text = "Description: ", required = False)
    route = forms.FileField()
