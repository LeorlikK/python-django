from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ShopModel

# Register your models here.
class ShopModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'model', 'price', 'get_photo', 'date_editing', 'date_publication', 'publication']
    list_display_links = ['name']
    search_fields = ['name',]
    list_editable = ['publication',]
    list_filter = ['publication', 'model', 'name']
    prepopulated_fields = {'slug': ('name',)}
    save_as = True
    save_on_top = True
    #readonly_fields = ['get_photo',]
    fields = ['name', 'slug', 'model', 'price', 'short_text', 'full_text', 'image', 'publication']
    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="30">')
        else:
            return 'Not'

    get_photo.short_description = 'Фотография'

admin.site.register(ShopModel, ShopModelAdmin)