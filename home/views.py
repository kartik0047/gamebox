from django.http import request
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate
from home.models import Register, Contact, Details, Requirements, Checkout, Order, Order_item
from django.contrib import messages
from .models import Games,Cart
#from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.hashers import  check_password
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta,date
# Create your views here.


# def login_user_required():
#     if not (request.session.get('email')):
#            return redirect("/loginUser")  

def index(request):
     #return render(request,'index.html')
     games_results = Games.objects.all() #select * from games tables
     return render(request, 'index.html', {'games_data':games_results})


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
    last_cust_id = Register.objects.latest('id')

   
    total_amount = 88
    created_date= date.today()
    status='0'
    bill=last_bill_id 
    customer=last_cust_id 

    order = Order(total_amount=total_amount, created_date=created_date, status=status, bill=bill, customer=customer)
    order.save()
    last_order_id = Order.objects.latest('id')
 
    qty=2
    sub_total=cart_total_amount
    order=last_order_id 
    
    order_item = Order_item(qty=qty, sub_total=sub_total, status=status, order=order)
    order_item.save()
    
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

def logoutUser(request):
    logout(request)
    return redirect("/login")

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


      