from django.urls import path
from . import views

urlpatterns = [
    path('buy-now/<int:product>/' ,views.buy_now, name='buy-now'),
    path('', views.orders, name='orders'),
    path('placing-the-order/<int:product>/', views.confirm_buy, name='confirm-buy')
]
