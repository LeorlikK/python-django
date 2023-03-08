from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Uhod_base, TestJson
from .models import CategoryUhod
from .forms import InputFindForm
from .utuls import MyMix
from django.core.paginator import Paginator

from django.http import JsonResponse
from django.core.serializers import serialize
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class ApiJson(View):

    # def json_create(self, request):
    #     TestJson.objects.create(name='RufusTwo', list_json={'two': 'twotwo'}, number=2)
    #     return redirect('news')

    def get(self, request):
        """Первый вариант"""
        # j = []
        # obj = TestJson.objects.filter(name='RufusTwo')
        # for item in obj:
        #     j.append({
        #         'name': item.name,
        #         'number': item.number,
        #         'list': item.list_json,
        #     })
        # data = {
        #     'all': j,
        # }
        #return JsonResponse(data)
        """Второй вариант"""
        obj = TestJson.objects.filter(name='RufusTwo')
        data = serialize('python', obj)
        del data[0]['model']

        """Третий вариант"""
        return JsonResponse({'data': data})

@method_decorator(csrf_exempt, name='dispatch')
def json_update(request, bot_command):
    """Обновление через JSON"""
    #if request.method == 'POST':
    if request.method == 'GET':
        dump =  json.loads(request.body)
        if dump['user']['password'] == '43ji-ws5f-38hf-h37a-8827-dh23-idj1':
            obj = TestJson.objects.get(name=dump['user']['name'])
            obj.list_json = dump['data']
            obj.save()
            return_json = {'update': 'successful'}
        else:
            return_json = {'update': 'fail >>> password error'}
    else:
        return_json = {'update': 'method error'}
    return JsonResponse(return_json)


@method_decorator(csrf_exempt, name='dispatch')
class BotApiView(View):
    """Обновление через URL"""
    def get(self, request, bot_command):
        if bot_command == 'read':
            if request.GET.get('password') == '43ji-ws5f-38hf-h37a-8827-dh23-idj1':
                pass
        elif bot_command == 'update':
            if request.GET.get('password') == '43ji-ws5f-38hf-h37a-8827-dh23-idj1':
                data = TestJson.objects.get(name=request.GET.get('name'))
                dump = {}

                for item in request.GET:
                    if item != 'name' and item != 'password': dump[str(item)] = (request.GET.get(item))

                data.list_json = dump
                data.save()
                return_json = {'update': 'successful'}
            else:
                return_json = {'update': 'fail >>> password error'}
        else:
            return_json = {'incorrect': 'command not found'}
        return JsonResponse(return_json)


    #return render(request, 'news/test2.html', {'data':data, 'rec': rec, 'context': context, 'pkk':pk})
    #return redirect('news')
    #return JsonResponse({'pkk':pk})
#'context': context,

def json_delete(request):
    data = TestJson.objects.get(name='Rufus')
    return render(request, 'news/test2.html', {'data':data})

class TestSearch(ListView):
    #model = Uhod_base
    context_object_name = 'news'
    template_name = 'news/test.html'
    paginate_by = 10
    allow_empty = True

    def get_queryset(self):
        if self.request.GET.get('s'):
            return Uhod_base.objects.filter(title__icontains=self.request.GET.get('s'))
        else:
            return Uhod_base.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['re'] =  self.request
        return context



def test1(request):
    category = CategoryUhod.objects.all()
    news = Uhod_base.objects.all()
    return render(request, 'news/test.html', {'news': news, 'category': category})

def test2(request, slug):
    pkk = CategoryUhod.objects.get(slug=slug).pk
    news = Uhod_base.objects.filter(category=pkk)
    # pkk = '1111111111111111111111'
    # news = CategoryUhod.objects.all()
    return render(request, 'news/test2.html', {'news': news, 'sl': slug})

def test3(request, pk):
    #detail = Uhod_base.objects.get(pk=pk)
    detail = Uhod_base.objects.filter(category__title='World of Warcraft')
    #two = CategoryUhod.objects.filter()
    return render(request, 'news/test2.html', {'detail': detail})


def test_input(request):
    data = request.GET.get('search', '')
    if data:
        find, page_obj = test_page(request, data)
        if len(find) > 0:
            b = CategoryUhod.objects.all()
            collection = {'text': data, 'all_category': b, 'data':data, 'page_obj': page_obj}
        else:
            b = CategoryUhod.objects.all()
            text = 'Ничего не найдено'
            collection = {'text': text, 'find': find, 'all_category': b, 'data':data}
        return render(request, 'news/news.html', collection)
    else:
        a, page_obj  = test_page(request, None)
        b = CategoryUhod.objects.all()
        text = 'Введите запрос...'
        collection = {'text': text, 'a': a, 'all_category': b, 'page_obj': page_obj}
    return render(request, 'news/news.html', collection)

def test_page(request, find):
    if find:
        object = Uhod_base.objects.filter(title__icontains=find, publication=True)
    else:
        object = Uhod_base.objects.filter(publication=True)
    p = Paginator(object, 1)
    page_num = request.GET.get('page')
    page_object = p.get_page(page_num)
    return object, page_object
# def test_input(request):
#     if request.method == 'POST':
#         data = InputFindForm(request.POST)
#         if data.is_valid():
#             form = InputFindForm()
#             input_user = data.cleaned_data['input_text']
#             find = Uhod_base.objects.filter(title=input_user)
#             if len(find) > 0:
#                 b = CategoryUhod.objects.all()
#                 text = 'Успех'
#                 collection = {'text': text, 'form': form, 'find': find, 'b': b}
#             else:
#                 b = CategoryUhod.objects.all()
#                 text = 'Ничего не найдено'
#                 collection = {'text': text, 'form': form, 'find': find, 'b': b}
#             return render(request, 'news/test.html', collection)
#         else:
#             form = InputFindForm()
#             text = 'Неверный запрос'
#             collection = {'text': text, 'form': form}
#     else:
#         page = test_page(request)
#         a = Uhod_base.objects.filter(publication=True)
#         b = CategoryUhod.objects.all()
#         form = InputFindForm()
#         text = 'Введите запрос...'
#         collection = {'text': text, 'form': form, 'a': a, 'b': b, 'page': page}
#     return render(request, 'news/test.html', collection)


    #return render(request, 'news/news.html', {'page_obj': page_object})

def osobennosti(request):
    return render(request, 'news/news.html')

def uhod(request):
    return render(request, 'news/news.html')

class UhodList(ListView):
    model = Uhod_base
    template_name = 'news/news.html'
    context_object_name = 'list'
    paginate_by = 1
    allow_empty = False

    def paginate_queryset(self, queryset, page_size):
        context = super().paginate_queryset(Uhod_base.objects.filter(publication=True), page_size)
        return  context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_category'] = CategoryUhod.objects.all()
        return context

    # def get_queryset(self):
    #     all_list = {
    #         'data': Uhod_base.objects.filter(publication=True),
    #         'category': CategoryUhod.objects.all(),
    #     }
    #     return all_list

class CategoryList(MyMix, ListView):
    model = Uhod_base
    template_name = 'news/news.html'
    context_object_name = 'b'
    paginate_by = 1
    allow_empty = False

    mixin_prop = '222'
    test_slug = '333'

    def paginate_queryset(self, queryset, page_size):
        #context = CategoryUhod.objects.get(slug=self.kwargs['slug'])
        context = super().paginate_queryset(Uhod_base.objects.filter(category=self.kwargs['pk'], publication=True), page_size)  # category=self.kwargs['slug']

        return  context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_category'] = CategoryUhod.objects.all()
        context['mixin_prop'] = self.give_me_page()
        context['test_slug'] = self.kwargs['pk']
        return context

    # def get_queryset(self):
    #     all_list = {
    #         'data': Uhod_base.objects.filter(category=self.kwargs['pk'], publication=True),
    #         'category': CategoryUhod.objects.all(),
    #         'id_category': self.kwargs['pk']
    #     }
    #     return all_list

class UhodDetail(DetailView):
    #model = Uhod_base
    template_name = 'news/news_detail.html'
    context_object_name = 'news_detail'

    def get_queryset(self):
        #return Uhod_base.objects.get(title='Худшая игра?')
        #return Uhod_base.objects.filter(pk=self.kwargs['pk'])
        return Uhod_base.objects.filter(pk=self.kwargs['pk'])
        #return Uhod_base.objects.all()

