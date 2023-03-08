from django.shortcuts import render, redirect
#from  django.http import HttpResponse
from .models import News_base
from .forms import News_baseForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.utils import timezone
# Create your views here.

def all_news2(request, pk):
    one = pk* 3 - 3
    two = pk* 3
    pk = pk+1
    data = News_base.objects.order_by('-date')[one:two]     #.all() #.get(id=1) #.filter(???_title__startswith = 'Какая')
                                                       #date = comment.all(если создан класс-привязка)
    text = {'text': 'Найти статью...'}
    return render(request, 'news/news.html', {'news_req': data, 'not_find': text, 'pkk': pk})

def find_news(request):
    #data = News_base.objects.filter(queryset_title__startswith = 'И')
    find = 'макрос'.title()
    data = News_base.objects.filter(title__icontains=find)
    #data = request.POST
    if data:
        text = {'text': 'Найти статью...'}
        return render(request, 'news/news.html', {'news_req': data, 'not_find': text})
    else:
        text = {'text': 'Ничего не найдено...'}
        return render(request, 'news/news.html', {'news_req': data, 'not_find': text})

def get(request, pk):
    data = News_base.objects.order_by('date')[:1]
    #return render(request, 'news/news.html', {'news_req': data})
    return render(request, 'news/get.html', {'get_news': data})
    #return render(request, 'news/get.html')

class NewsDetailView(DetailView):
    model = News_base
    template_name = 'news/once_news.html'
    context_object_name = 'news_get'

class NewsUpdateView(UpdateView):
    model = News_base
    template_name = 'news/update.html'
    form_class = News_baseForm

class NewsDeleteView(DeleteView):
    model = News_base
    template_name = 'news/news-delete.html'
    success_url = '/news/'

def all_news(request):
    data = News_base.objects.order_by('-date')[:3]     #.all() #.get(id=1) #.filter(???_title__startswith = 'Какая')
                                                       #date = comment.all(если создан класс-привязка)
    text = {'text': 'Найти статью...'}
    return render(request, 'news/news.html', {'news_req': data, 'not_find': text})

def create_news(request):
    type_er = request
    if request.method == 'POST':
        form  = News_baseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_news')
        else:
            error = "Error form"
    else:
        error = 'Ошибочка!'

    form = News_baseForm()
    data = {
        'form': form,
        'er': error,
        'type': type_er
    }
    return render(request, 'news/create_news.html', data)