from django import forms
from buddyapp.models import Route

class UploadRouteForm(forms.Form):
    title = forms.CharField(max_length = 50)
    route = forms.FileField()
