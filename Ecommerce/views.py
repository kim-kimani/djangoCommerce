from django.shortcuts import get_object_or_404, render
from Category.models import Category
from .models import Products

# Create your views here.
def store(request, category_slug=None):
    current_category = None
    products = None
    
    if category_slug != None:
        current_category = get_object_or_404(Category, category_slug=category_slug)
        products = Products.objects.filter(category=current_category, is_available=True)
    else:
        products = Products.objects.all().filter(is_available=True)
        
    categories = Category.objects.all()
    product_count = products.count()
    
    context = {
        'products': products,
        'categories': categories,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Products.objects.get(category__category_slug=category_slug, product_slug=product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)


