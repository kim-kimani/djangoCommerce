from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def get_url(self):
        return reverse('products_by_category', args=[self.category_slug])
    
    def __str__(self):
        return self.category_name
    

