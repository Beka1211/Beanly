from django.contrib import admin
from .models import Brand,Category,Product,Storage,Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')   
    search_fields = ('name',)      


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_available', 'created_at')
    list_filter = ('is_available', 'category')  
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'rating')
    search_fields = ('user', 'product')
