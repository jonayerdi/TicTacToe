from django import forms
from django.contrib.auth.models import User

class CreateUserForm(forms.Form):

    def validate_name(value):
        try:
            user = User.objects.get(username=value)
        except Exception:
            user = None
        if user != None:
            raise forms.ValidationError(
                (' Username %(value)s is already taken'),
                params={'value': value},
            )
            
    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password != password2:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data
        
    username = forms.CharField(max_length=150, label='User name', required=True, validators=[validate_name])
    password = forms.CharField(max_length=32, label='Password', required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=32, label='Password again', required=True, widget=forms.PasswordInput)
                
        