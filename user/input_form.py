from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

phone_validator = RegexValidator(r'^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$')

class LoginForm(forms.Form):
    phone = forms.CharField(max_length=15, required=True, validators=[phone_validator], widget=forms.TextInput(attrs={'placeholder':'Phone Number'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    


class SignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=20, required=True, validators=[phone_validator], widget=forms.TextInput(attrs={'placeholder':'Phone Number'}))
    password1 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation'}))

    class Meta:
        model = User
        fields = ['phone', 'password1', 'password2']
