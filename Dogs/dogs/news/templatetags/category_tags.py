from django import template

from news.models import CategoryUhod

register = template.Library()

@register.simple_tag()
def get_all_category():
    return CategoryUhod.objects.all()