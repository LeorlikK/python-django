# def input(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user=user)
#             return redirect('main')
#     else:
#         form = UserLoginForm()
#     return render(request, 'login/input.html', {'form': form})

# for item in self.fields:
#     self.fields[str(item)].widget.attrs.update({'class': 'testone'})

# {% block page %}
#     {% for name  in page_obj.object_list %}
#         <p>{{ name.title }}</p>
#         <p>{{ name.anons }}</p>
#         <p>{{ name.date_publication }}</p>
#     {% endfor %}
#     {% for page in page_obj.paginator.page_range %}
#         <a href="?page={{ page }}">{{ page }}</a>
#     {% endfor %}
# {% endblock %}

#def get_context_data(self,*args,**kwargs):

# raise +
#_include +
#hasattr +
#kwargs, args +
#*   ** +
#slug
#Mixins +
#isinstance +
#= not self.obj +
#q = a if a is not None else self.a +



# декораторы
# revers/e
# кэш
# truncatewords_html:20|safe
# if page_obj.has_other_pages   # paginator.page_range  # number # if page_obj.has_next

#paginator
#page_obj
#is_paginated
#object_list
import os
import time

import requests
import json



class One:

    def __init__(self, *args):
        self.model1 = args

    def one(self):
        print(*self.model1)
        return self.model1

class Two(One):

    def __init__(self, *args):
        super().__init__(*args)
        self.model2 = args

    def two(self):
        print(*self.model2)
        return self.model2

class Three( Two,One):
    def __init__(self):
        super().__init__()
        self.model3 = 3

    def three(self):
        print(self.model3)

#one = One()

class Five:

    def __init__(self):
        self.five = 5


    def sum(self, num):
        print('Class Five')
        return self.five + num

class Six(Five):

    def __init__(self):
        super(Six, self).__init__()
        self.six = 6

    def sum(self, num):
        t = 5 + 13
        print(t)
        m = super().sum(num)
        print(222)
        b = self.six + num
        return m, b


#six = Six()


"""Вариант URL"""
# url = "http://127.0.0.1:8000/bots/"
# name = str('Bot_2')
# password = str('43ji-ws5f-38hf-h37a-8827-dh23-idj1')
# command = 'update'
# content = {'position': [1600, 1200], 'state': 'active', 'count_farm': 562}
# real_url = f"{url}{command}/?name={name}&password={password}"
# for key, value in content.items():
#     real_url += f'&{str(key)}={str(value) if isinstance(value, (str, int)) else f"{str(value[0])},{str(value[1])}"}'
# print(real_url)
# data = requests.get(real_url ).json()
# print(data)


"""Вариант JSON"""
# url = "http://127.0.0.1:8000/bots/"
# command = 'update2'
# content = {
#     'user': {
#         'name': 'Bot_2',
#         'password': '43ji-ws5f-38hf-h37a-8827-dh23-idj1',
#     },
#     'data': {
#         'position': [1900, 1200],
#         'state': 'active',
#         'count_farm': 560,
#     },
# }
# #content = json.dumps(content)
# real_url = f"{url}{command}/"
# print(real_url)
# #data = requests.post(real_url, json=content).json()
# data = requests.get(real_url, json=content).json()
# print(data)




# hasattr
# two = Two(1,2,3,'Tom')
# print(two.__dir__())
# if hasattr(two, 'model1'):
#     print('Yes')
# else:
#     print('No')
#
# a = 'Hello'
# if isinstance(a, int):
#     print('Yes2')
# else: print('No')

# def __init__(self, **kwargs):
#     """
#     Constructor. Called in the URLconf; can contain helpful extra
#     keyword arguments, and other things.
#     """
#     # Go through keyword arguments, and either save their values to our
#     # instance, or raise an error.
#     for key, value in kwargs.items():
#         setattr(self, key, value)

# Методы миксинов

"""Тест JSON"""
massive1 = {
    'one': 'str',
    'two': 4,
    'three': 5.56,
    'four': True,
    'five': [1, 2, 3, 4],
    'six': {
        'six_a': None,
    }
}

# massive1 = json.dumps(massive1)
# massive2 = 'WoW is a beast game!'
# a = open('write.txt', 'w', encoding='utf-8')
# a.write(massive1)
# a.close()
# with open('write.txt', 'r', encoding='utf-8') as file:
#     massive1 = file.read()
#     massive1 = json.loads(massive1)
#     print(massive1)
#     print(massive1['one'])

# dump = json.dumps(massive1)
# print(type(dump))
# print(dump)
# load = json.loads(dump)
# print(load)
# with open('json_massive', 'w', encoding='utf-8') as file:
#     json.dump(dump, file)
# time.sleep(1)
# with open('json_massive', 'r', encoding='utf-8') as file:
#     m = json.load(file)
#     print(m)
#     print(type(m))
#     m = json.loads(m)
#     print(m)
#     print(type(m))
# res = m['four']
# print(res)

"""Микро тест request"""
#res = requests.post()
for  valter in massive1.items():
    #print(item)
    print(valter[0])
    print(valter, '\n')

one = 13
two = one%2
print(two)

"""Тест декоратора"""
#         print('Finish')
#
#     return two
#
# @cry
# def say():
#     print('Hello World')
# say()

# def test(func, *args, **kwargs):
#     t0 = time.time()
#     func(*args, **kwargs)
#     return print(time.time() - t0)
#
# def run(*args, **kwargs):
#     for item in range(*args):
#         print(item)
#         time.sleep(1)
#     for i, val in kwargs.items():
#         print(i, val)
# test(run, 5, title='Hello', name='Igor')

# def decor(func):
#     def wripper(*args, **kwargs):
#         time0= time.time()
#         finish = func(*args, **kwargs)
#         time1 = time.time() - time0
#         return time1, finish
#     return wripper
#
# @decor
# def circle(num):
#     for item in range(num):
#         print(item)
#         time.sleep(1)
#     return 'I am other'
# a, b = circle(5)
# print(a, b)

# from pathlib import Path
# #way = os.path.abspath('test.py')
# way = Path(__file__).resolve().parent.parent
# print(way)
# way1 = os.path.join(way, 'music')
# print(way1)