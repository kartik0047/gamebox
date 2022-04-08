from django.contrib import admin

# Register your models here.

from .models import Games,Contact,Details,Requirements,Checkout,Register,Order,Order_item,Coupons,Send_email,OTP,Wishlist

class GamesAdmin(admin.ModelAdmin):
     list_display = ('name', 'image','price' )
admin.site.register(Games, GamesAdmin)

class ContactAdmin(admin.ModelAdmin):
     list_display = ('name', 'email','phone', 'comment' )
admin.site.register(Contact, ContactAdmin)

class RegisterAdmin(admin.ModelAdmin):
     list_display = ('id','name', 'email','phone', 'password' )
admin.site.register(Register, RegisterAdmin)

class DetailsAdmin(admin.ModelAdmin):
     list_display = ('name', 'genre', 'release_date','developer', 'publisher','platform','modes' )
admin.site.register(Details, DetailsAdmin)

class RequirementsAdmin(admin.ModelAdmin):
     list_display = ('name', 'os', 'processor','memory', 'graphics','storage')
admin.site.register(Requirements, RequirementsAdmin)

class CheckoutAdmin(admin.ModelAdmin):
     list_display = ('id','fname', 'lname', 'email','phone', 'address','state','city', 'pin')
admin.site.register(Checkout, CheckoutAdmin)

class OrderAdmin(admin.ModelAdmin):
     list_display = ('id','customer', 'total_amount', 'created_date','bill_address', 'status')
admin.site.register(Order, OrderAdmin)

class Order_itemAdmin(admin.ModelAdmin):
     list_display = ('id','customer','image','games', 'qty','price','status') 
admin.site.register(Order_item, Order_itemAdmin)

class WishlistAdmin(admin.ModelAdmin):
     list_display = ('id','customer','games','status') 
admin.site.register(Wishlist, WishlistAdmin)

class CouponsAdmin(admin.ModelAdmin):
     list_display = ('code', 'valid_from', 'valid_to', 'discount', 'active')
admin.site.register(Coupons, CouponsAdmin)

class Send_emailAdmin(admin.ModelAdmin):
     list_display = ('subject', 'message', 'email_from', 'recipient_list')
admin.site.register(Send_email, Send_emailAdmin)

class OTPAdmin(admin.ModelAdmin):
     list_display = ('otp', 'date')
admin.site.register(OTP, OTPAdmin)
     

