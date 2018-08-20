from django import forms
from django.db import models


class SignupForm(forms.Form):

      name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class' : 'input100'}))
      phone= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class' : 'input100'}))
      group= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'How Many People', 'class' : 'input100'}))
