from django.shortcuts import render,redirect
from .models import Category, Product, Customer, Order, Request
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, ProductForm, AddressForm
from django.db.models import Q
#import HttpResponse
from django.http import HttpResponse
import requests
import json 
# from django.core.mail import send_mail
# from django.core.mail import EmailMessage
# from django.conf import settings
# Create your views here.
@login_required(login_url='login')
def category(request,foo):
    try:
        category=Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products, 'category':category})
    except:
        messages.success(request,("category doesn't exist........"))
        return redirect('home')
@login_required(login_url='login')
def product(request,pk):
    products = Product.objects.get(id=pk)
    return render(request,'product.html',{'products': products})
@login_required(login_url='login')
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request,'home.html',{'products': products, 'categories': categories})
@login_required(login_url='login')
def profile(request):
    customer = request.user.customer
    addresses = customer.address_set.all()
    address = addresses[0]
    return render(request,'profile.html',{'customer': customer, 'address': address})
    # return redirect('profile')
@login_required(login_url='login')
def orders(request):
    # products = Product.objects.all()
    # orders = Order.objects.filter(customer=request.user.customer)
    orders = request.user.customer.order_set.all()
    return render(request,'orders.html',{'orders': orders})
    # return redirect('profile')
@login_required(login_url='login')
def order_expanded(request,pk):
    # deliveries = Order.objects.filter(product__seller=request.user.customer)
    # seller_details=deliveries.get(id=pk)
    customer = request.user.customer
    addresses = customer.address_set.all()
    address = addresses[0]
    ordered = Order.objects.get(id=pk)
    return render(request,'order_expanded.html',{'ordered': ordered , 'customer': customer, 'address': address })
@login_required(login_url='login')
def my_requests(request):
    accepted_requests = request.user.customer.request_set.filter(status='accepted')
    rejected_requests = request.user.customer.request_set.filter(status='rejected')
    pending_requests = request.user.customer.request_set.filter(status='pending')
    return render(request,'my_requests.html',{'accepted_requests': accepted_requests , 'rejected_requests': rejected_requests , 'pending_requests': pending_requests})
@login_required(login_url='login')
def success_requests_expanded(request,pk):
    # deliveries = Order.objects.filter(product__seller=request.user.customer)
    # seller_details=deliveries.get(id=pk)
    customer = request.user.customer
    addresses = customer.address_set.all()
    address = addresses[0]
    requested = Request.objects.get(id=pk)
    return render(request,'success_requests_expanded.html',{'requested': requested , 'customer': customer, 'address': address })
@login_required(login_url='login')
def products(request):
    products= request.user.customer.product_set.all()
    # products = Product.objects.all()
    return render(request,'products.html',{'products': products})
@login_required(login_url='login')
def deliveries(request):
    deliveries = Order.objects.filter(product__seller=request.user.customer)
    return render(request,'deliveries.html',{'deliveries': deliveries})
    # deliveries_expanded
@login_required(login_url='login')
def deliveries_expanded(request,pk):
    # customer = request.delivery.customer
    delivery = Order.objects.get(id=pk)
    addresses = delivery.customer.address_set.all()
    address = addresses[0]
    return render(request,'deliveries_expanded.html',{'delivery': delivery , 'address': address })
@login_required(login_url='login')
def product_upload(request,pk):
    product = Product.objects.get(id=pk)
    # products = request.user.customer.product_set.all()
    return render(request,'product_upload.html',{'product': product})
@login_required(login_url='login')
def about(request):
    # Product.objects.all().delete()
    # Category.objects.all().delete()
    # res = requests.get('https://fakestoreapi.com/products/categories')
    # response = json.loads(res.text)
    # for x in response:
    #     Category.objects.create(name= x)
    # res = requests.get('https://fakestoreapi.com/products')
    # response = json.loads(res.text)
    # # print(response)
    # for x in response:
    #     category = Category.objects.get_or_create(name=x['category'])[0]
    #     Product.objects.create(p_name=x['title'], price=x['price'], category=category, description=x['description'], image=x['image'], is_sale=True, sale_price=x['price']*0.8)
    #     Product.objects.create(p_name=x['title', ])
    
    # res = requests.get('https://fakestoreapi.com/products')
    # response = json.loads(res.text)
    # print(response)
    # for x in response:
    #     url= x['image']
    #     resp = requests.get(url)
    #     with open('media/products/'+str(x['id'])+'.jpg', 'wb') as f:
    #         f.write(resp.content)
    #     category = Category.objects.get_or_create(name=x['category'])[0]
    #     Product.objects.create(p_name=x['title'], price=x['price'], category=category, description=x['description'], image=x['image'], is_sale=True, sale_price=x['price']*0.8)
    # return render(request,'about.html')
    # res = requests.get('https://fakestoreapi.com/products')
    # response = json.loads(res.text)
    # # print(response)
    # for x in response:
    #     category = Category.objects.get_or_create(name=x['category'])[0]
    #     Product.objects.create(p_name=x['title'], price=x['price'], category=category, description=x['description'], image='products/'+str(x['id'])+'.jpg', is_sale=True, sale_price=x['price']*0.8)
    return render(request,'about.html')
    # return redirect('home')

def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("you have beeen logged in ..."))
            return redirect('home')
        else:
            messages.success(request,("bad credentials, try again ..."))
            return redirect('login')
    return render(request,'login.html')
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request,("you have beeen logged out ..."))
    return redirect('home')
#function for checking if email entered is already in use in registration view
def is_email_present(email):
    try:
        customer=User.objects.get(email=email)
        return False
    except:
        return True
def register_user(request):
    form = SignUpForm()
    form1 = AddressForm()
    if request.method == "POST":
        print('post requested....')
        form = SignUpForm(request.POST)
        form1 = AddressForm(request.POST)
        if form.is_valid() and form1.is_valid():
            # form.save()
            print('form is valid....')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            if(is_email_present(email)):
                #checking if user already exists
                user=authenticate(username=username,password=password,email=email)
                # print(user)
                if user is None:     
                    print('creating user....')     
                    user = form.save()    
                    customer=Customer.objects.create(
                    user=user,
                    # city=form.cleaned_data['city'],
                    phone=form.cleaned_data['phone']
                    )
                    address = form1.save(commit=False)
                    customer.save()
                    address.customer = customer
                    print('creating address....')
                    address.save()
                    login(request,user)
                    # emailObject = EmailMessage(
                    #     'Thanks for registering into Acraiders',
                    #     'We are happy to have you onboard',
                    #     settings.EMAIL_HOST_USER,
                    #     [email],
                    # )
                    # emailObject.send(fail_silently=True)
                    messages.success(request,("you have Registered ..."))
                    return redirect('home')
                else:
                    messages.success(request,("Sorry, couldn't reach server. Please try again...."))
            else:
                messages.success(request,("Sorry...... entered email is already in use. Try logging in....or enter new email...."))
                return redirect('register')
        else:
            # messages.success(request,("Whoops...... Form data is invalid...."))
            messages.success(request,(str(form.errors)))
            return redirect('register')
    else:     
        return render(request,'register.html',{'form':form, 'form1':form1})
@login_required(login_url='login')
def search(request):
    if request.method == "POST":
        search = request.POST['search']
        res = Product.objects.filter(Q(p_name__icontains=search) | Q(description__icontains=search))
    return render(request,'search.html',{'products':res, 'searched':search})
@login_required(login_url='login')
def sell(request):
    form = ProductForm()
    if request.method == "POST":
        print('post requested....')
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            print('form is valid....')
            pending_seller=form.save(commit=False)
            # print(pending_seller)
            # pending_seller["seller"]= (request.user).customer
            try:
                # customer = Customer.objects.get(user=request.user)
                # pending_seller.seller= customer
                # print(pending_seller)
                pending_seller.seller = request.user.customer
                pending_seller.save()
                messages.success(request,("product has been Registered ..."))
                return redirect('sell')
            except Customer.DoesNotExist:
                messages.success(request,("Sorry...... User is not a customer, please try again from other account...."))
                return redirect('sell')
            
        else:
            # messages.success(request,("Whoops...... Form data is invalid...."))
            messages.success(request,(str(form.errors)))
            # return json.dumps({'status':'form error'})
            return redirect('sell')
            # return redirect('register')
    else:     
        return render(request,'sell.html',{'form':form})
@login_required(login_url='login')
def buySuccess(request):
    return render(request,'buySuccess.html')
@login_required(login_url='login')
def buyFailure(request):
    return render(request,'buyFailure.html')  
@login_required(login_url='login')
def buy(request):
    print("hi")
    if request.method == "POST":
        print('post requested....')
        try:
            # return render(request,'buySuccess.html')
            product_id = request.POST['product_id']
            print(product_id)
            product = Product.objects.get(id=product_id)
            product_price = product.sale_price
            print(product_price)
            product_qty = request.POST['product_qty']
            print(product_qty)
            #compare integer values of product_qty and product_price
            #cast string to its integer value
            product_qty = int(product_qty)
            product_price = int(product_price)
            if product_qty>product.quantity :
                messages.success(request,("Sorry, that much quantity is not available."))
                return HttpResponse(status=400)
            cost = product_price * int(product_qty)
            print(cost)
            customer = request.user.customer
            pending_order = Order()
            pending_order.product = Product.objects.get(id=product_id)
            pending_order.customer = request.user.customer
            pending_order.quantity = product_qty
            pending_order.cost = cost
            # print(pending_order)
            print('order created')
            pending_order.save()
            messages.success(request,("buy successful..."))
            # we have to return status code 200 to ajax call
            # return json.dumps({'status':'success'})
            return HttpResponse(status=200)
            print("hi")
        except Exception as e:
            print(e)
            messages.success(request,("buy failure..."))
            return HttpResponse(status=400)
    else:
        return redirect('home')   
@login_required(login_url='login')
def request(request):
    if request.method == "POST":
        print('post requested....')
        try:
            product_id = request.POST['product_id']
            print(product_id)
            # product = Product.objects.get(id=product_id)
            product_qty = request.POST['product_qty']
            product_qty = int(product_qty)
            print(product_qty)
            customer_message = request.POST['customer_message']
            print(customer_message)
            product_cost = int(request.POST['product_cost'])
            print(product_cost)
            # customer = request.user.customer
            pending_request = Request()
            pending_request.product = Product.objects.get(id=product_id)
            pending_request.customer = request.user.customer
            pending_request.quantity = product_qty
            pending_request.cost = product_cost
            pending_request.customer_message = customer_message
            pending_request.save()
            messages.success(request,("request successful..."))
            return redirect('my_requests')
        except Exception as e:
            print(e)
            messages.success(request,("request failure...try again..."))
            return HttpResponse(status=400)
    else:
        return redirect('home')