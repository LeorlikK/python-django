from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

def all_biography(request):
    data = {
        'title': "News Page!!!",
        'array': ['News1', 'News2', 'News3']
    }
    return render(request, 'biography/biography.html', data)

def yennefer_biography(request):
    return render(request, 'biography/yennefer.html')

def triss_biography(request):
    return render(request, 'biography/triss.html')
