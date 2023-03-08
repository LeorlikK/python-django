from .models import News_base
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class News_baseForm(ModelForm):
    class Meta:
        model = News_base
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title' : TextInput(attrs={
                'class': 'form-test',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-test',
                'placeholder': 'Анонс статьи'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-test form-test-two',
                'placeholder': 'Текст статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-test',
                'placeholder': 'Дата публикации'
            })
        }