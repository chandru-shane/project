from django.urls import path
from . import views


urlpatterns = [
    path('addingcart/<int:product>/', views.add_to_cart, name='add-cart'),
    path('',views.cart, name='cart'),
]
