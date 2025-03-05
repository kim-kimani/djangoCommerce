from django.contrib import admin
from .models import Products, Variation

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug': ('product_name',)}
    list_display = ('product_name', 'category', 'modified_date', 'price', 'stock', 'is_available')
    list_editable = ('is_available', 'stock')
    
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

admin.site.register(Products, ProductsAdmin)
admin.site.register(Variation, VariationAdmin)