from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Games(models.Model):
    name=models.CharField(max_length=200,null=True)
    image= models.ImageField((""), upload_to='myimage', height_field=None, width_field=None, max_length=None)
    price =  models.IntegerField(blank=True, null=True)
     
    def __str__(self):
        return str(self.name)

class Register(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=10,null=True)
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Register.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Register.objects.filter(email = self.email):
            return True

        return  False

    def __str__(self):
        return "%s %s" % (self.id,self.name)   
    
class Contact(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    comment = models.TextField(null=True) 

class Details(models.Model):
    name = models.ForeignKey(Games, on_delete=models.CASCADE, null=True)
    genre=models.CharField(max_length=200,null=True)
    release_date = models.DateField()
    developer=models.CharField(max_length=200,null=True)
    publisher = models.CharField(max_length=200,null=True)
    platform = models.CharField(max_length=200,null=True)
    modes = models.CharField(max_length=200,null=True)

class Requirements(models.Model):
    name = models.ForeignKey(Games, on_delete=models.CASCADE, null=True)
    os=models.CharField(max_length=200,null=True)
    processor=models.CharField(max_length=200,null=True)
    memory = models.CharField(max_length=200,null=True)
    graphics = models.CharField(max_length=200,null=True)
    storage = models.CharField(max_length=200,null=True)

class Cart(models.Model): 
    customer=models.OneToOneField(Register, null=True, on_delete=models.CASCADE)  
    games=models.ManyToManyField(Games)    

    def __str__(self):
        return str(self.customer)
 
class Checkout(models.Model):
    fname= models.CharField(max_length=200,null=True)
    lname= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    phone= models.CharField(max_length=200,null=True)
    address= models.TextField(null=True)
    state= models.CharField(max_length=200,null=True)
    city= models.CharField(max_length=200,null=True)
    pin =models.CharField(max_length=200,null=True)

    def __str__(self):
        return "%s %s" % (self.id,self.fname)
    
class Order(models.Model):
    customer= models.ForeignKey(Register, on_delete=models.CASCADE, blank=True, null=True)
    total_amount= models.CharField(max_length=200,null=True)
    created_date= models.DateField(null=True)
    bill_address= models.ForeignKey(Checkout, on_delete=models.CASCADE, null=True)
    status= models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
class Order_item(models.Model):
    customer= models.ForeignKey(Register, on_delete=models.CASCADE, blank=True, null=True)
    image= models.ImageField((""), upload_to='myimage', height_field=None, width_field=None, max_length=None,null=True)
    qty= models.CharField(max_length=5,null=True)
    price= models.CharField(max_length=200,null=True)
    games = models.CharField(max_length=200,null=True)
    status= models.BooleanField(default=False)

    def __str__(self):
        return str(self.customer)

class Wishlist(models.Model): 
    customer= models.ForeignKey(Register, on_delete=models.CASCADE, null=True)
    games = models.ForeignKey(Games, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=True)
 
class Coupons(models.Model):
    code= models.CharField(max_length=50, unique=True)
    valid_from= models.DateTimeField()
    valid_to= models.DateTimeField()
    discount= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active= models.BooleanField()

    def _str_(self):
        return self.code

class Send_email(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField(null=True)
    email_from = models.CharField(max_length=50)
    recipient_list = models.CharField(max_length=50)

class OTP(models.Model):
    otp = models.IntegerField()
    date = models.DateTimeField()



