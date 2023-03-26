from django.contrib import admin
from django.urls import path, include

from app_shop import views



urlpatterns = [
    path('', views.index, name="home"),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('add_product', views.add_product, name='add_product'), 
    path('product_view_<int:p_id>', views.product_view, name='product_view'),
    path('your_cart', views.your_cart, name='your_cart'),
    path('login_', views.login_, name='login_'),
    path('signup_', views.signup_, name='signup_'),
    path('profile', views.profile, name='profile'),
    

] 