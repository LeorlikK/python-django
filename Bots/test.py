"""План
- css
- кнопка назад
- форма для добавляения бота

- как через запрос изменить данные в базе???
"""
import json
import requests
import os

# a =  os.path.abspath('skjfhsdjfhsdjfh')
# print(os.path.abspath('test.py'))
# print(os.path.dirname('test.py'))
# b = os.path.join(a) + 'test.py'
# c = os.path.join(a, 'test.py')
# print(b)
# print(c)


#a = os.path.join()

# t = {"settings": 123456789}
# with open('test.json', 'w', encoding='utf-8') as file:
#     json.dump(t, file, indent=4, ensure_ascii=False)

# with open('test.json', 'r', encoding='utf-8') as file:
#     text = json.load(file)
#     print(text)

# url_get = 'http://127.0.0.1:8000/info/1'
# res = requests.get(url_get).text
# print(res)

# url_post = 'http://127.0.0.1:8000/3'
# res = requests.get(url_post).text
# print(res)

url_create = 'http://127.0.0.1:8000/create'
url_read = 'http://127.0.0.1:8000/read'
url_update = 'http://127.0.0.1:8000/update'
url_delete = 'http://127.0.0.1:8000/delete'
res = requests.get(url_update).text
print(res)
