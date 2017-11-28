from django import forms
from buddyapp.models import Route

class UploadRouteForm(forms.Form):
    name = forms.CharField(max_length = 50, help_text="Name: ")
    description = forms.CharField(max_length = 300, help_text = "Description: ")
    route = forms.FileField()
