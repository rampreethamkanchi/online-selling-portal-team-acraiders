# Create your models here.
from django.db import models
from django.core.validators import RegexValidator

# from django.utils.text import slugify
from django.contrib.auth.models import User
import datetime
from phonenumber_field.modelfields import PhoneNumberField
from indian_cities.dj_city import cities
# from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(default='', blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
def get_default_category():
    return Category.objects.get_or_create(name='Miscellaneous and Others')[0].id

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=20, choices=cities)
    phone = PhoneNumberField()

    def __str__(self):
        return str(self.user)
class Manager(models.Model):
    gender_choices = [
        ('male','male'),
        ('female','female'),
        ('others','others'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=20, choices=cities)
    phone = PhoneNumberField()
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    pincode = models.CharField(
        max_length=6,
        validators=[RegexValidator('^[0-9]{6}$', 'Invalid postal code')],
    )
    street = models.CharField(max_length=50)
    house_no = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField()
    gender = models.CharField(max_length=50, choices=gender_choices)
    locality = models.CharField(max_length=50)
    #add to Managers group
    # user.groups.add(Group.objects.get(name='Managers'))
    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name_plural = 'managers'
    def save(self, *args, **kwargs):
        # Call the parent class's save method
        super().save(*args, **kwargs)
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.save(update_fields=['is_superuser', 'is_staff'])

# @receiver(post_save, sender=Manager)
# def manager_created(sender, instance, created, **kwargs):
#     if created:
#         g = Group.objects.get(name='Manager')
#         g.user_set.add(instance.user)
#         print('Manager added to Managers group')
class Product(models.Model): 
    id = models.AutoField(primary_key=True)
    p_name = models.CharField("Product name",max_length=100)
    m_name = models.CharField("Name of the manufacturing company",max_length=100, default='unknown', blank=True)
    seller = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_price = models.PositiveBigIntegerField(default=0)
    # price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    price = models.PositiveBigIntegerField(default=0)
    #set default category to others
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=get_default_category)
    description = models.TextField()
    #upload upto 5 images to f"products/{id}/" folder
    image1 = models.ImageField(upload_to="products/")
    image2 = models.ImageField(upload_to="products/", default='products/default_product.png',blank=True)
    image3 = models.ImageField(upload_to="products/", default='products/default_product.png',blank=True)
    image4 = models.ImageField(upload_to="products/", default='products/default_product.png',blank=True)
    image5 = models.ImageField(upload_to="products/", default='products/default_product.png',blank=True)
    city = models.CharField(max_length=20, choices=cities)
    age = models.DurationField("Age of product",default=datetime.timedelta(0),blank=True)
    # quantity = models.IntegerField(default=1,blank=True)
    quantity = models.PositiveBigIntegerField(default=1,blank=True)
    # age = models.TimeField(default=datetime.time(0, 0))
    # slug = models.SlugField(unique=True, max_length=100,)

    # Add sales stuff
    is_sale = models.BooleanField(default=True)
    # sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)


    def __str__(self):
        return self.p_name
class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.CharField(max_length=20, choices=cities)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    pincode = models.CharField(
        max_length=6,
        validators=[RegexValidator('^[0-9]{6}$', 'Invalid postal code')],
    )
    street = models.CharField(max_length=50)
    house_no = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.city
    class Meta:
        verbose_name_plural = 'addresses'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    cost= models.PositiveBigIntegerField()
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
    cost= models.PositiveBigIntegerField()
    date = models.DateField(default=datetime.date.today, blank=True)
    # status = models.BooleanField(default=False,blank=True)
    # status = models.CharField(max_length=50,default='pending')
    status = models.CharField(max_length=50, choices=status_choices, default='pending')
    # customer_message = models.TextField(blank=True,default='no message')
    # seller_message = models.TextField(blank=True,default='no message')

    def __str__(self):
        return str(self.product)
    
class Chat(models.Model):
    message = models.TextField(blank=True, default='no message')
    created_at = models.DateTimeField(default=timezone.now)
    #customer who created this message
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.message)
