from django.contrib import admin

# Register your models here.

from .models import Games,Contact,Details,Requirements,Checkout,Register,Order,Order_item

class GamesAdmin(admin.ModelAdmin):
     list_display = ('name', 'image','price' )
admin.site.register(Games, GamesAdmin)

class ContactAdmin(admin.ModelAdmin):
     list_display = ('name', 'email','phone', 'comment' )
admin.site.register(Contact, ContactAdmin)

class RegisterAdmin(admin.ModelAdmin):
     list_display = ('name', 'email','phone', 'password' )
admin.site.register(Register, RegisterAdmin)

class DetailsAdmin(admin.ModelAdmin):
     list_display = ('name', 'genre', 'release_date','developer', 'publisher','platform','modes' )
admin.site.register(Details, DetailsAdmin)

class RequirementsAdmin(admin.ModelAdmin):
     list_display = ('name', 'os', 'processor','memory', 'graphics','storage')
admin.site.register(Requirements, RequirementsAdmin)

class CheckoutAdmin(admin.ModelAdmin):
     list_display = ('fname', 'lname', 'email','phone', 'address','state','city', 'pin')
admin.site.register(Checkout, CheckoutAdmin)

class OrderAdmin(admin.ModelAdmin):
     list_display = ('customer', 'total_amount', 'created_date','bill', 'status')
admin.site.register(Order, OrderAdmin)

class Order_itemAdmin(admin.ModelAdmin):
     list_display = ('order', 'qty', 'sub_total', 'status')
admin.site.register(Order_item, Order_itemAdmin)

