from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product
# Create your views here.

@login_required
def buy_now(request,product):
    product = Product.objects.get(id=product)
    if request.method == 'POST':
        return 
    return render(request, 'orders/buy_now.html', {'product':product})

