from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from Ecommerce.models import Products, Variation
from .models import Cart, CartItem

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Products.objects.get(id=product_id) #get the product
    # product_variation = []
    # if request.method == 'POST':
    #     for item in request.POST:
    #         key = item
    #         value = request.POST[key]
            
    #         try:
    #             variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
    #             product_variation.append(variation)
    #         except:
    #             pass       
        
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()
    
    is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
    if is_cart_item_exists:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()

    return redirect('cart')
    # if is_cart_item_exists:
    #     cart_item = CartItem.objects.filter(product=product, cart=cart)
    #     ex_var_list = []
    #     for item in cart_item:
    #         existing_variation = item.variations.all()
    #         ex_var_list.append(existing_variation)
            
    #     print(ex_var_list)
        
    #     if product_variation in ex_var_list:
    #         return HttpResponse('Product already in cart')
    #     else:
    #         return HttpResponse('False')
        
    #     if len(product_variation) > 0:
    #         cart_item.variations.clear()
    #         for item in product_variation:
    #             cart_item.variations.add(item)
    #     # cart_item.quantity += 1  #cart_item.quantity = existing quantity + 1
    #     # cart_item.save()
        
    # else:
    #     cart_item = CartItem.objects.create(
    #         product = product,
    #         quantity = 1,
    #         cart = cart,
    #     )
    #     if len(product_variation) > 0:
    #         cart_item.variations.clear()
    #         for item in product_variation:
    #             cart_item.variations.add(item)
    #     cart_item.save()
    
    # return redirect('cart')

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart')

def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Products, id = product_id)
    cart_item = CartItem.objects.get(product = product, cart = cart)
    cart_item.delete()
    
    return redirect('cart')
    

def cart(request, total=0, quantity=0, cart_items=None):
    total_tax=0
    general_total=0
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            if cart_item.product.offer_price:
                cart_item.price_per_item = cart_item.product.offer_price
            else:
                cart_item.price_per_item = cart_item.product.price
            cart_item.total = cart_item.price_per_item * cart_item.quantity
                
            total += cart_item.total
            quantity += cart_item.quantity
            total_tax = round(total * 0.16, 2)
            general_total = round(total + total_tax)
    except Cart.DoesNotExist:
        pass
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'total_tax': format(total_tax, '.2f'),
        'general_total': general_total,
    }
    return render(request, 'store/cart.html', context)


