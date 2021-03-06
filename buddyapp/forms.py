from django import forms
from buddyapp.models import Route, UserProfile
from django.contrib.auth.models import User

class UploadRouteForm(forms.Form):
    name = forms.CharField(max_length = 50)
    description = forms.CharField(max_length =140, required = False)
    route = forms.FileField()

class  UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class  UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ('website', 'picture')
"""
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
            fields = ('title', 'url', 'views')
        """
