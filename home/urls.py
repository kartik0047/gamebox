"""HP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
           path('',views.index, name='index'),
           path('contact', views.contact,name='contact'),
           path('register',views.registerUser, name='register'),
           path('login',views.loginUser, name='login'),
           path('details/<game_id>/<game_name>',views.game_details, name='game-details'),
           path('logout', views.logoutUser,name='logout'),

           #ADD TO CART
           path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
           path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
           path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
           path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
           path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
           path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
           path('checkout',views.checkout, name='checkout'),
           path('confirm_order',views.confirm_order, name='checkout'),
           path('payment/<cart_total_amount>',views.payment, name='payment'),
           
]

