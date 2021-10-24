from django.urls import path
from . import views


urlpatterns = [
    path('addingcart/<int:product>/', views.add_to_cart, name='add-cart'),
    path('',views.cart, name='cart'),
    path('delete/<int:id>/', views.delete_cart,name='delete-cart'),
    path('singlecheckout/<int:id>/', views.checkout_single_cart, name='single-checkout'),
    path('checkoutall/', views.checkout_all, name='checkout-all')
]
