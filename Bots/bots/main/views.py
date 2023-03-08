from django.shortcuts import render, get_object_or_404, redirect
from .models import Table_base, Table_base_two, Table_base_three
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse
from .forms import Table_base_Form, Table_base_Form_two, Test_input_base

# Create your views here.
import json

def test_input(request):
    if request.method == 'POST':
        form = Table_base_Form_two(request.POST)
        if form.is_valid():
            input = form.cleaned_data['text_input']
            data = Table_base.objects.filter(name=input)
            return render(request, 'main/main_page.html', {'data': data})
    if request.method == 'GET':
        form = Table_base_Form_two()
        return render(request, 'main/find.html', {'form': form})

def test_img(request):
    data = Table_base_three.objects.all()
    return render(request, 'main/table_three.html', {'content': data})
"""CRAD"""

"""CREATE"""
class BorCreateView(CreateView):
    model = Table_base
    fields = []

def add_bot(request):
    if request.method == 'POST':
        form = Table_base_Form(request.POST)
        if form.is_valid():
            form.save()
            data = Table_base.objects.all()
            return render(request, 'main/main_page.html', {'data': data})
        else:
            data = Table_base.objects.all()
            return render(request, 'main/main_page.html', {'data': data})

    # if request.method == 'GET':
    #     form = Table_base_Form()
    #     return render(request, 'main/form_create.html', {'form': form})

def add_1(request):
    if request.method == 'GET':
        bot_2 = Table_base(state='Unactive', name='Two', position='1300, 700', all_res='2')
        bot_2.save()
        #bot_3 = Table_base.objects.create(state='Unactive', name='Three', position='1300, 700', all_res='2')
        return HttpResponse({'GET': 123, })

"""READ"""
class BotDetailView(DetailView):
    model = Table_base
    template_name = 'main/bot_detail.html'
    context_object_name = 'bot_info'

def test_bot(request, pkk):
    data = Table_base.objects.get(id=pkk)
    return render(request, 'main/bot_detail.html', {'bot_info': data})

def read_1(request):
    func_name = 'main'
    #data = Table_base.objects.all()
    #data = Table_base.objects.filter(name='One')
    data = Table_base.objects.order_by('-a2')[:5]
    #data = Table_base.objects.get(name='One')
    #data = Table_base.objects.exclude(name='One')
    #data = get_object_or_404(Table_base, )
    if request.method == "POST":
        form = Table_base_Form()
        form_in = Table_base_Form_two()
        post = request.POST
        return render(request, 'main/main_page.html',
                      {'data': data, 'func_name': func_name, 'form': form, 'from_in': form_in, 'post': post})
    else:
        form = Table_base_Form()
        form_in = Table_base_Form_two()
        return render(request, 'main/main_page.html',
                      {'data': data, 'func_name': func_name, 'form': form, 'from_in':form_in})

def find(request):
    form = Table_base_Form_two()
    return render(request, 'main/form_create.html', {'form': form})

def read_2(request, bot_pk):
    func_name = 'main'
    data = get_object_or_404(Table_base, pk=bot_pk)
    return render(request, 'main/bot_detail.html', {'bot_info': data, 'func_name': func_name})

"""UPDATE"""
class NewsUpdateView(UpdateView):
    model = Table_base
    template_name = 'news/update.html'
    #form_class = News_baseForm

def update_1(request):
    # bot = Table_base.objects.get(id='3')
    # bot.name = 'Three'
    # bot.save()

    bot = Table_base.objects.filter(name='Two').update(position='50, 50')
    return bot

"""DELETE"""
class NewsDeleteView(DeleteView):
    model = Table_base
    template_name = 'news/news-delete.html'
    success_url = '/news/'

def delete_1(request):
    bot = Table_base.objects.get(id='4')
    bot.delete()
    return bot


