from django.contrib import admin
from .models import Uhod_base, CategoryUhod, TestJson
from django.utils.safestring import mark_safe

# Register your models here.
class Uhod_base_Admin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'category', 'title', 'date_editing', 'date_publication', 'publication', 'get_photo']
    list_display_links = ['category', 'title']
    search_fields = ['title',]
    list_editable = ['publication']
    list_filter = ['publication', 'category']
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    save_on_top = True
    readonly_fields = ['get_photo']
    fields = ['publication', 'slug', 'category', 'title', 'anons', 'full_text', 'get_photo',]

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="30">')
        else:
            return 'Not'

    get_photo.short_description = 'Фото'

class CategoryUhod_Admin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'title',]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Uhod_base, Uhod_base_Admin)
admin.site.register(CategoryUhod, CategoryUhod_Admin)
admin.site.register(TestJson)