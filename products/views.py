from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product
# Create your views here.

@login_required
def home(request):
    products = Product.objects.all()
    return render(request,'products/home.html',context={'products':products})

@login_required
def detail_view(request, product):
    product = Product.objects.get(id=product)
    return render(request, 'products/detail_page.html', context={'product':product})