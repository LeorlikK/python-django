from django.contrib import admin
from .models import Table_base, Table_base_two, Table_base_three, Category

# Register your models here.

class Table_base_Admin(admin.ModelAdmin):
    list_display = ('state', 'name', 'category', 'all_res', 'position', 'a1', 'a2')
    list_display_links = ('state', 'name')
    search_fields = ('name', 'state')

class Category_Admin(admin.ModelAdmin):
    list_display = ('title', 'id')
    list_display_links = ('title', 'id')
    search_fields = ('title',)

admin.site.register(Table_base, Table_base_Admin)
admin.site.register(Table_base_two)
admin.site.register(Table_base_three)
admin.site.register(Category, Category_Admin)