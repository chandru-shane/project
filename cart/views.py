from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from orders.models import Order
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

@login_required
def delete_cart(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('cart')



@login_required
def checkout_single_cart(request, id):
    if (
        not request.user.profile.phone 
        or not request.user.profile.address 
        or not request.user.profile.pincode
    ):
        messages.warning(request,'Please Update your profile address!')
        return redirect('profile')    
        
    cart = Cart.objects.get(id=id)
    
    
    cart_items = cart.quantity
    cart_total = cart.product.price * cart_items
    discount_price = cart.product.discount * cart_items
    
    order = Order.objects.create(user=request.user, total=discount_price)
    for i in range(cart_items):
        order.products.add(cart.product)
    order.save()

    return redirect('orders')


@login_required
def checkout_all(request):
    if (
        not request.user.profile.phone 
        or not request.user.profile.address 
        or not request.user.profile.pincode
    ):
        messages.warning(request,'Please Update your profile address!')
        return redirect('profile')    
        
    carts = Cart.objects.filter(user=request.user)
    
    if len(carts) == 0:
        messages.warning(request,'Nothing in the cart!')
        return redirect('cart')
    
    order = Order.objects.create(user=request.user,total=0)
    total = 0
    discount = 0
    for cart in carts:
        cart_items = cart.quantity
        for i in range(cart_items):
            order.products.add(cart.product)
            total += cart.product.price
            discount += cart.product.discount
    order.total = discount
    carts.delete()
    return redirect('orders')
