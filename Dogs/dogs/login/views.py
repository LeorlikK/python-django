from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout

# Create your views here.

def input_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user=user)
            gc = f'Добро пожаловать {user}'
            return render(request, 'main/index.html', {'gc': gc})
        else:
            messages.error(request, 'Неверный логин или пароль')
    else:
        form = UserLoginForm()
    return render(request, 'login/input.html', {'form': form})

def logout_user(request):
        logout(request)
        return redirect('main')

def registration_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user=user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('registration')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'login/registration.html', {'registration_form': form})
