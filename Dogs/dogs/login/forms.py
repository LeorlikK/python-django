from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


#class UserInputForm
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'testone'}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'testone'}))

    #fields = ['username', 'password']
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for item in self.fields:
    #         #data_class =
    #         self.fields[str(item)].widget.attrs.update({'class': 'testone'})
    #         self.fields[str(item)].widget.attrs.update({'class': 'testone'})

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Любые буквы', widget=forms.TextInput(attrs={'class': 'testone'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'testone'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'testone'}))
    email = forms.EmailField(label='Адрес электронной почты', widget=forms.EmailInput(attrs={'class': 'testone'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']