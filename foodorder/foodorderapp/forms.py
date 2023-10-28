from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']

class userlogin(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


