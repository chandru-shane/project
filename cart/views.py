from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Cart
# Create your views here.

@login_required
def add_to_cart(request,product):
    
    product = Product.objects.get(id=product)
    try:
        cart = Cart.objects.filter(product=product,user=request.user)
        if len(cart)==0:
            raise ObjectDoesNotExist
        cart = cart[0]
        cart.quantity += 1
        cart.save()
    except ObjectDoesNotExist:
        cart = Cart.objects.create(product=product, user=request.user)
    
    return redirect('cart')

@login_required
def cart(request):
    carts = Cart.objects.filter(user=request.user)
    cart_items = 0
    cart_total = 0
    discount_price = 0
    for cart in carts:
        cart_items += cart.quantity
        cart_total += cart.product.price * cart.quantity
        discount_price += cart.product.discount * cart.quantity
        

    cart_summary = {
        'items':cart_items,
        'total':cart_total,
        'discount':discount_price
    }
    return render(request,'cart/cart.html', {'carts':carts, 'cart_summary':cart_summary})