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
           path('forgot_password',views.forgot_password, name='forgot_password'),
           path('reset_password',views.reset_password, name='reset_password'),
           path('change_password',views.change_password, name='change_password'),
           path('my_orders',views.my_orders, name='my_orders'),
           path('clear_my_orders',views.clear_my_orders, name='clear_my_orders'),
           path('email_check',views.email_check, name='email_check'),
           path('enter_OTP',views.enter_OTP, name='enter_OTP'),
           path('verify_OTP',views.verify_OTP, name='verify_OTP'),
           path('details/<game_id>/<game_name>',views.game_details, name='game-details'),
           path('logout', views.logoutUser,name='logout'),
           path('chart', views.main_view,name='chart'),
           path('coupons', views.coupons,name='coupons'),
           path('coupon_apply', views.coupon_apply,name='coupon_apply'),
           path('subscribe', views.subscribe,name='subscribe'),
           path('add_to_wishlist/<game_id>', views.add_to_wishlist, name='add_to_wishlist'),
           path('view_wishlist', views.view_wishlist, name='view_wishlist'),
           path('wishlist_clear', views.wishlist_clear, name='wishlist_clear'),

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

