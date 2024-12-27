from django.forms import ModelForm
from django import forms

from . models import Passwd

class PmForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Passwd
        fields=['name','link','password','userid']
        exclude=['userid']
