from django.contrib import admin
from django.urls import path, include
from app_ecom import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('home', views.index, name='index'), 
    path('services', views.services, name='services'), 
    path('contact', views.contact, name='contact'), 
    path('about', views.about, name='about'), 
    path('cart', views.cart, name='your_cart'),
    path('product_view<int:p_id>', views.product_view, name='products'),  
]