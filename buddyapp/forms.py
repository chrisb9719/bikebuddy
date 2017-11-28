from django import forms
from buddyapp.models import Route, UserProfile
from django.contrib.auth.models import User

class UploadRouteForm(forms.Form):
    name = forms.CharField(max_length = 50, help_text="Name: ", required = True)
    description = forms.CharField(max_length =140, help_text = "Description: ", required = False)
    route = forms.FileField()

class  UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class  UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
