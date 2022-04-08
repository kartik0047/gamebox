from atexit import register
from email import message
from sqlite3 import Date
from django import forms
from django.http import HttpResponse, request
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate
from home.models import Register, Contact, Details, Requirements, Checkout, Order, Order_item, OTP, Wishlist
from django.contrib import messages
from .models import Coupons, Games, Cart
#from django.contrib.auth.decorators import login_required
from cart.cart import Cart
#from coupons.forms import CouponApplyForm
import matplotlib.pyplot as plt
from .utils import get_plot
from django.contrib.auth.hashers import  check_password
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta, date, timezone
from django.conf import settings
import math, random
from django.core.mail import send_mail

# Create your views here.

# def login_user_required():
#     if not (request.session.get('email')):
#            return redirect("/loginUser")  

def index(request):
     if not (request.session.get('email')):
           return redirect("/loginUser")  
     games_results = Games.objects.all() #select * from games tables
     return render(request, 'index.html', {'games_data':games_results})

def header(request):
    pass
    return render(request, 'header.html')

def coupons(request):
     return render(request, 'coupons.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def enter_OTP(request):
    return render(request, 'enter_OTP.html')

def my_orders(request):
    
    my_order = Order_item.objects.all()
    return render(request,'my_orders.html' ,{'order_list':my_order})

def clear_my_orders(request,id):
     if not (request.session.get('email')):
           return redirect("/loginUser")  
     else:
        my_order = Order_item(request)
        my_order.clear()
        return redirect("my_orders")

def contact(request):
     if request.method=="POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          contact=request.POST.get('contact')
          comment=request.POST.get('comment')

          con = Contact(name=name, email=email, phone=contact, comment=comment )
          con.save()
          messages.success(request,"Your message has been sent successfully.")
     return render(request,'contact.html') 

def checkout(request):
     if request.method=="POST":
          request.session['bill_fname'] = request.POST.get('fname')
          request.session['bill_lname'] = request.POST.get('lname')
          request.session['bill_email'] = request.POST.get('email')
          request.session['bill_phone'] = request.POST.get('phone')
          request.session['bill_address'] = request.POST.get('address')
          request.session['bill_state'] = request.POST.get('state')
          request.session['bill_city'] = request.POST.get('city')
          request.session['bill_pin'] = request.POST.get('pin')

         # check = Checkout(fname=fname, lname=lname, email=email, phone=phone, address=address, state=state, city=city, pin=pin)
         # check.save()
          return redirect("/confirm_order")  

     return render(request,'checkout.html') 

def payment(request,cart_total_amount):
    data = request.session['cart']
    email = request.session['email']
    customer_data = Register.get_customer_by_email(email)
    cust_id = request.session['id'] = customer_data.id
   
    for data_list in data.values():
     game_name = data_list['name']
     game_qty = data_list['quantity']
     game_price = data_list['price']
     game_iamge = data_list['image']

    fname=request.session.get('bill_fname')
    lname=request.session.get('bill_lname')
    email=request.session.get('bill_email')
    phone=request.session.get('bill_phone') 
    address=request.session.get('bill_address') 
    state=request.session.get('bill_state')
    city=request.session.get('bill_city')
    pin=request.session.get('bill_pin')
    
    check = Checkout(fname=fname, lname=lname, email=email, phone=phone, address=address, state=state, city=city, pin=pin)
    check.save()
    last_bill_id = Checkout.objects.latest('id')

    total_amount = cart_total_amount
    created_date = date.today()
    status = '0'
    bill_address = last_bill_id 
    customer_id = cust_id 
    
    order = Order(total_amount=total_amount, created_date=created_date, status=status, bill_address=bill_address, customer_id=customer_id)
    order.save()
    last_order_id = Order.objects.latest('id')
    
    email = request.session['email']
    customer_data = Register.get_customer_by_email(email)
    #cust_id = request.session['id'] = customer_data.id

    #order = last_order_id

    for data_list in data.values():
     order_item = Order_item(image=data_list['image'], qty=data_list['quantity'], price=data_list['price'], status=status, customer_id=customer_id, games= data_list['name'])
     order_item.save()

    # del request.session['cart']
     
    return render(request,'index.html') 

def registerUser(request):
     if request.method=="POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          pwd=request.POST.get('password')
          phone=request.POST.get('phone')
          password = make_password(pwd)  
          register = Register(name=name, email=email, password=password, phone=phone )
          register.save()
          messages.success(request,"Your registration has been done successfully.")
          
     return render(request,'registeration.html')  

# def loginUser(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         #print(username, password)

#         # check if user has entered correct credentials
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             # A backend authenticated the credentials
#             login(request, user)
#             return redirect("/")

#         else:
#             # No backend authenticated the credentials
#             return render(request, 'login.html')

#     return render(request, 'login.html')

def loginUser(request):
    
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Register.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['email'] = customer.email
                request.session['id'] = customer.id
                return redirect('index')
                # if loginUser.return_url:
                #     return HttpResponseRedirect(loginUser.return_url)
                # else:
                #     loginUser.return_url = None
                #     return redirect('index')
            else:
                    error_message = 'Email or Password invalid !!'
        else:
                error_message = 'Email or Password invalid !!'

        #print(email, password)
        return render(request, 'login.html', {'error': error_message})
    return render(request, 'login.html')

def logoutUser(request):
     
    del request.session['email']
    return redirect("login")

def generateOTP():

    digits = "0123456789"
    OTP = ""
    print("OTP Generation")
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

if __name__ == "__main__":
  print("OTP of 6 digits:", generateOTP())
 
def email_check(request):
    email = request.POST.get('email')
    customer = Register.get_customer_by_email(email)
    request.session['email'] = email
    error_message = None
    otp = generateOTP()
    date = datetime.today()
    if  customer:
        subject = 'Reset Your Password'
        message = 'Your OTP is' + ' ' + otp
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['kartikc6147@gmail.com'] 
        send_mail( subject, message, email_from, recipient_list )
        otp = OTP(otp=otp,date=date)
        otp.save()
        return render(request, 'enter_OTP.html')
    else:
       error_message = 'Email id does not exist !!'

    return render(request, 'forgot_password.html', {'error': error_message})

def verify_OTP(request):
     if request.method=="POST":
            otp = request.POST.get('otp')
            #error_message = None
            #verified_message = None
            try: 
                check_otp = OTP.objects.get(otp=otp)
                #print('hii')
                #verified_message = 'Your OTP is verified successfully..'
                return render(request, 'reset_password.html')
            except: 
                error_message = 'Sorry, Wrong OTP!!!'
                return render(request, 'enter_OTP.html',{'error': error_message})

def reset_password(request):
    new_password = request.POST.get('new_password')
    confirm_password = request.POST.get('confirm_password')
    email = request.session['email']
    #print(email)
    verified_message = "Your Password Is Changed Successfully.."
    if request.method=="POST":
        if  new_password == confirm_password:
            Register.objects.filter(email=email).update(password= make_password(confirm_password)) #update field
           # password = Register.objects.get(email=email).update(password=confirm_password)
           # password.value = confirm_password  # change field
           # password.save() # this will update only
            return render(request, 'login.html')
        else:
             verified_message = "Your Password Is Changed Successfully.."
             return render(request, 'reset_password.html', {'verify': verified_message}) #{'error': error_message})
            #error_message = "Password Doesn't Match!!"
    return render(request, 'reset_password.html', {'verify': verified_message}) #{'error': error_message})

def change_password(request):
    return render(request, 'change_password.html')
 
def game_details(request,game_id,game_name):
    
    game_results = Games.objects.get(id=game_id) #select * from games tables where id='game_id'
    details_results = Details.objects.get(name_id=game_id)
    game_info = Requirements.objects.get(name_id=game_id) 
    return render(request, 'details.html', {'games_da':game_results,'games_details':details_results,'game_info':game_info})

def cart_add(request, id):
    if not (request.session.get('email')):
           return redirect("/login")  
    else:
        cart = Cart(request)
        game = Games.objects.get(id=id)
        cart.add(product=game)
        return redirect("cart_detail")

def item_clear(request, id):
    if not (request.session.get('email')):
           return redirect("/loginUser")  
    else:
        cart = Cart(request)
        game = Games.objects.get(id=id)
        cart.remove(game)
        return redirect("cart_detail")

def item_increment(request, id):
    if not (request.session.get('email')):
           return redirect("/loginUser")  
    else:
        cart = Cart(request)
        game= Games.objects.get(id=id)
        cart.add(product=game)
        return redirect("cart_detail")


def item_decrement(request, id):
    if not (request.session.get('email')):
           return redirect("/loginUser")  
    else:
        cart = Cart(request)
        game = Games.objects.get(id=id)
        cart.decrement(product=game)
        return redirect("cart_detail")

def cart_clear(request):
    if not (request.session.get('email')):
           return redirect("/loginUser")  
    else:
        cart = Cart(request)
        cart.clear()
        return redirect("cart_detail")

def cart_detail(request):

    if not (request.session.get('email')):
           return redirect("/loginUser")  
    else:
        return render(request, 'cart_detail.html')  

def confirm_order(request,):
    if not (request.session.get('email')):
           return redirect("/loginUser")  
    else:
        cid=request.session.get('id')
        user_results = Register.objects.get(id=cid) #select * from games tables where id='game_id'
        #checkout_result = Checkout.objects.get(id=64) #select * from games tables where id='game_id'
        return render(request, 'confirm_order.html', {'login_ifno':user_results})  

def main_view(request):
    qs = Games.objects.all()
    x = [x.name for x in qs]
    y = [y.price for y in qs]
    #plt.plot(y, linestyle = 'dotted')
    #plt.show()
    chart = get_plot(x,y)
    return render(request, 'admin_black/templates/admin/index.html',{'chart': chart })

def coupon_apply(request):
    if request.method=="POST": 
        coupon_code = request.POST.get('code')
        coupon_results = Coupons.objects.get(code=coupon_code)
        return render(request, 'cart_detail.html', {'coupon_info':coupon_results})
    return redirect("cart_detail")

def subscribe(request):
    subject = 'welcome to GFG world'
    message = 'Hi Hello User.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['kartikc6147@gmail.com'] 
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse('<h1>email has been sent.</h1>' + email_from)

def add_to_wishlist(request,game_id):

        email = request.session['email']
        customer_data = Register.get_customer_by_email(email)
        cust_id = request.session['id'] = customer_data.id

        checkw=Wishlist.objects.filter(customer_id=cust_id, games_id=game_id).count()
        if checkw > 0:
            messages.error(request, 'This item has been already added.')
        else:        
            wish = Wishlist(customer_id=cust_id, games_id=game_id, status=1)
            wish.save()
        return render(request,'index.html')

def view_wishlist(request):

    game_results = Wishlist.objects.all()
    return render(request,'wishlist.html', {'games_da':game_results})

def wishlist_clear(request):
    if not (request.session.get('email')):
           return redirect("/loginUser")  
    else:
        wishlist = Wishlist(request)
        wishlist.clear()
        return redirect("wishlist")
