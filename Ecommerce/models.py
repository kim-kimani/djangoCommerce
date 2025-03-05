from django.db import models
from django.urls import reverse
from Category.models import Category

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    product_slug = models.SlugField(unique=True, blank=True, null=True)
    product_description = models.TextField(max_length=1000, blank=True)
    price = models.IntegerField(default=0)
    offer_price = models.IntegerField(default=0, blank=True, null=True)
    product_images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    def get_url(self):
        return reverse('product_detail', args=[self.category.category_slug, self.product_slug])
    
    def __str__(self):
        return self.product_name

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)
    
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)
    
    
variation_category_choices = (
    ('color', 'Color'),
    ('size', 'Size'),
)
class Variation(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=50, choices=variation_category_choices)
    variation_value = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    objects = VariationManager()
    
    def __str__(self):
        return self.variation_value
    

