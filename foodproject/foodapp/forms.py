from django.forms import forms
from django import forms
from .models import foodtab

class foods(forms.ModelForm):
    class Meta:
        model = foodtab
        fields = ['name','ingre','desc','image']