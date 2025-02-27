from django.shortcuts import get_object_or_404, render
from Category.models import Category
from .models import Products
from Cart.models import CartItem
from Cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def store(request, category_slug=None):
    current_category = None
    products = None
    
    if category_slug != None:
        current_category = get_object_or_404(Category, category_slug=category_slug)
        products = Products.objects.filter(category=current_category, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    else:
        products = Products.objects.all().filter(is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        
    categories = Category.objects.all()
    product_count = products.count()
    
    context = {
        'products': paged_products,
        'categories': categories,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Products.objects.get(category__category_slug=category_slug, product_slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)


