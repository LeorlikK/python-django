import os

from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.views.generic import ListView

from glasses.settings import BASE_DIR
from .models import ShopModel


# Create your views here.
def test(request):
    return render(request, 'index/index.html')

class MainPage(ListView):
    model = ShopModel
    template_name = 'index/test.html'
    context_object_name = 'data'
    allow_empty = True
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['way'] = os.path.join(BASE_DIR, 'index\static\media')
        return context