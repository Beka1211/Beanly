from django.contrib import admin
from .models import Brand,Category,Product,Storage,Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'is_available', 'created_at')
    list_filter = ('is_available', 'category')  
    search_fields = ('title', 'description')
    ordering = ('-created_at',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock')
    search_fields = ('stock',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'rating')
    search_fields = ('user', 'product')
