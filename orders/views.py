from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from orders.models import Order
# Create your views here.

@login_required
def buy_now(request,product):
    product = Product.objects.get(id=product)
    return render(request, 'orders/buy_now.html', {'product':product})

@login_required
def confirm_buy(request,product):
    product = Product.objects.get(id=product)
    if (
        not request.user.profile.phone 
        or not request.user.profile.address 
        or not request.user.profile.pincode
    ):
        messages.warning(request,'Please Update your profile address!')
        return redirect('profile')   
    order = Order.objects.create(user=request.user,total=product.discount)
    order.products.add(product)
    order.address = request.user.profile.address
    order.phone = request.user.profile.phone
    order.pincode = request.user.profile.pincode
    order.save()

    return redirect('orders')

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')
    return render(request, 'orders/orders.html', {'orders':orders})