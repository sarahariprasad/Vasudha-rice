from django.contrib import admin

from .models import Category, Product, PosterView


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'variety','brand','slug','weight', 'price','discont_price', 'description',
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'discont_price','in_stock']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PosterView)
class PosterAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

