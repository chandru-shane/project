from django.urls import path
from . import views

urlpatterns = [
    path('buy-now/<int:product>/' ,views.buy_now, name='buy-now'),
]
