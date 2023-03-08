from django import forms
from .models import Table_base, Test_input_base
from django.db import models

class Table_base_Form(forms.ModelForm):
    class Meta:
        model = Table_base
        fields = ['state', 'name', 'position', 'all_res']

        widgets = {
            'state': forms.TextInput(attrs={
                'class': 'form-test',
                'placeholder': 'Статус'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-test',
                'placeholder': 'Имя'
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-test',
                'placeholder': 'Позиция'
            }),
            'all_res': forms.TextInput(attrs={
                'class': 'form-test',
                'placeholder': 'Кол-во ресурсов'
            }),
        }

class Table_base_Form_two(forms.ModelForm):
    class Meta:
        model = Test_input_base
        fields = ['text_input',]

        widgets = {
            'text_input': forms.TextInput()
        }



