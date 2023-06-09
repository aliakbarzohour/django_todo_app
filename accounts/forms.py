from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=100)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()