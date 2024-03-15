from django.shortcuts import render,redirect
from .models import Category, Product, Customer, Order
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, ProductForm
from django.db.models import Q
import requests
import json 
# Create your views here.
def category(request,foo):
    try:
        category=Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products, 'category':category})
    except:
        messages.success(request,("category doesn't exist........"))
        return redirect('home')
def product(request,pk):
    products = Product.objects.get(id=pk)
    return render(request,'product.html',{'products': products})
def home(request):
    products = Product.objects.all()
    return render(request,'home.html',{'products': products})

def about(request):
    # Product.objects.all().delete()
    # Category.objects.all().delete()
    # res = requests.get('https://fakestoreapi.com/products/categories')
    # response = json.loads(res.text)
    # for x in response:
    #     Category.objects.create(name= x)
    # res = requests.get('https://fakestoreapi.com/products')
    # response = json.loads(res.text)
    # print(response)
    # for x in response:
    #     category = Category.objects.get_or_create(name=x['category'])[0]
    #     Product.objects.create(p_name=x['title'], price=x['price'], category=category, description=x['description'], image=x['image'], is_sale=True, sale_price=x['price']*0.8)
        # Product.objects.create(p_name=x['title', ])
    
    # res = requests.get('https://fakestoreapi.com/products')
    # response = json.loads(res.text)
    # # print(response)
    # for x in response:
    #     url= x['image']
    #     resp = requests.get(url)
    #     with open('media/products/'+str(x['id'])+'.jpg', 'wb') as f:
    #         f.write(resp.content)
        # category = Category.objects.get_or_create(name=x['category'])[0]
        # Product.objects.create(p_name=x['title'], price=x['price'], category=category, description=x['description'], image=x['image'], is_sale=True, sale_price=x['price']*0.8)
    # return render(request,'about.html')
    # res = requests.get('https://fakestoreapi.com/products')
    # response = json.loads(res.text)
    # print(response)
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
            messages.success(request,("you have beeen logged in ..."))
            return redirect('login')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("you have beeen logged out ..."))
    return redirect('home')
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        print('post requested....')
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user=authenticate(username=username,password=password,email=email)
            if user is not None:               
                customer=Customer.objects.create(
                user=user,
                city=form.cleaned_data['city'],
                phone=form.cleaned_data['phone']
                )
                customer.save()
                login(request,user)
                messages.success(request,("you have Registered ..."))
                return redirect('home')
            else:
                messages.success(request,("Sorry...... There was problem in registering, please try again...."))
                return redirect('register')
        else:
            # messages.success(request,("Whoops...... Form data is invalid...."))
            messages.success(request,(str(form.errors)))
            return redirect('register')
    else:     
        return render(request,'register.html',{'form':form})
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
    