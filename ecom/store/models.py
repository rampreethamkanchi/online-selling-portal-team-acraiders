# Create your models here.
from django.db import models
# from django.utils.text import slugify
from django.contrib.auth.models import User
import datetime



class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(default='', blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
def get_default_category():
    return Category.objects.get_or_create(name='others')[0].id

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # city = models.CharField(max_length=50,null=True, blank=True)
    phone = models.CharField(max_length=50,null=True, blank=True)
    # email = models.EmailField(max_length=50)
    # password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)

class Product(models.Model):  # Renamed from Products to Product (singular)
    p_name = models.CharField(max_length=100)
    seller = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    # price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    price = models.PositiveBigIntegerField(default=0)
    #set default category to others
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=get_default_category)
    description = models.TextField()
    image = models.ImageField(upload_to='products/',null=True, blank=True)
    city = models.CharField(max_length=50,null=True, blank=True)
    age = models.DurationField(default=datetime.timedelta(0),blank=True)
    quantity = models.IntegerField(default=1,blank=True)
    # age = models.TimeField(default=datetime.time(0, 0))
    # slug = models.SlugField(unique=True, max_length=100,)

    # Add sales stuff
    is_sale = models.BooleanField(default=True)
    sale_price = models.PositiveBigIntegerField(default=0)
    # sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)


    def __str__(self):
        return self.p_name
class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.CharField(max_length=50,)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50)
    house_no = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.city
    class Meta:
        verbose_name_plural = 'addresses'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cost= models.PositiveBigIntegerField(default=0)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    # phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.date.today, blank=True)
    status = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return str(self.product)
    
class Request(models.Model):
    #3 status: pending, accepted, rejected may be as enum
    status_choices = [
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cost= models.PositiveBigIntegerField(default=0,blank=True)
    date = models.DateField(default=datetime.date.today, blank=True)
    # status = models.BooleanField(default=False,blank=True)
    # status = models.CharField(max_length=50,default='pending')
    status = models.CharField(max_length=50, choices=status_choices, default='pending')
    customer_message = models.TextField(blank=True,default='no message')
    seller_message = models.TextField(blank=True,default='no message')

    def __str__(self):
        return str(self.product)
