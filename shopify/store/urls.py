from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [

    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('product-detail', views.index, name='product-detail'),
    path('order', views.order, name='order'),
    path('cart', views.cart, name='cart'),
    path('register', views.register, name='register'),

]
