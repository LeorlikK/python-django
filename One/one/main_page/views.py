
from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
# from django.urls import path
# mod = path.insert(0, "D:\Python\Django\One\one\news")
# import mod

def index(request):
    data = {
        'title': "Вопрос жизни и смерти!",
        'array': ['Choose your fate', 'Hi-Hi', '123']
    }
    return render(request, 'main_page/index.html', data)

def biography(request):
    return render(request, 'biography/biography.html')

def news(request):
    return render(request, 'news/news.html')



