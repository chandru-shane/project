from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:product>/', views.detail_view, name='detail-view'),
]
