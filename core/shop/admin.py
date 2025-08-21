from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')   
    search_fields = ('name',)      


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_available', 'created_at')
    list_filter = ('is_available', 'category')  
    search_fields = ('name', 'description')      # поиск по имени и описанию
    ordering = ('-created_at',)                  # сортировка по дате создания

