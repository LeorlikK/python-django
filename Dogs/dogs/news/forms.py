from django import forms
#from .models import
from django.db import models

class InputFindForm(forms.Form):
    input_text = forms.CharField(max_length=250)
        #fields = ['input_text', ]
