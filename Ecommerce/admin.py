from django.contrib import admin
from .models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug': ('product_name',)}
    list_display = ('product_name', 'category', 'modified_date', 'price', 'stock', 'is_available')

admin.site.register(Products, ProductsAdmin)