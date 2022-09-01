from django.contrib import admin

from products.models import Category, Product


class AdminCategory(admin.ModelAdmin):
    list_display_1 = ['title', 'image', 'price', 'category']


class AdminProduct(admin.ModelAdmin):
    list_display_2 = ['title', 'image', 'price', 'category']


# Register your models here.
admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
