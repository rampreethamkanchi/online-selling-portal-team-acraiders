from django.shortcuts import render,redirect
from .models import Category, Product, Customer, Order, Request,Chat,Issue
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
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            update_session_auth_hash(request,form.user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            send_email(user.email,'Alert! Password changed','Your password has been changed successfully. If you did not make this change, please contact us immediately. You can login here http://localhost:8000/login')
            return redirect('profile')
        else:
            messages.success(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
def send_email(email,subject, message):
    emailObject = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
            )
    emailObject.send(fail_silently=True)
    print("sent, mail successfully")
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
    customer_is_seller = True
    can_deliver = True
    #check if customer can request for product, by checking 
    #if product is not owned by customer
    if products.seller != request.user.customer:
        customer_is_seller = False
    if not products.is_light:
        seller_address = products.seller.address_set.all()[0]
        customer_address = request.user.customer.address_set.all()[0]
        print(seller_address.city)
        print(customer_address.city)

        if seller_address.city != customer_address.city:
            print("not same city")
            can_deliver = False
        # if products.seller.city != request.user.customer.city:
        #     can_deliver = False
    return render(request,'product.html',{'products': products,'can_deliver':can_deliver, 'customer_is_seller':customer_is_seller})
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
def edit_profile(request):
    customer = request.user.customer
    addresses = customer.address_set.all()
    address = addresses[0]
    return render(request,'edit_profile.html',{'customer': customer, 'address': address})
@login_required(login_url='login')
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
    seller = ordered.product.seller
    return render(request,'order_expanded.html',{'ordered': ordered , 'customer': customer, 'address': address, 'seller':seller })
@login_required(login_url='login')
def my_requests(request):
    accepted_requests = request.user.customer.request_set.filter(status='accepted')
    rejected_requests = request.user.customer.request_set.filter(status='rejected')
    pending_requests = request.user.customer.request_set.filter(status='pending')
    return render(request,'my_requests.html',{'accepted_requests': accepted_requests , 'rejected_requests': rejected_requests , 'pending_requests': pending_requests})
@login_required(login_url='login')
def negotiate_expanded(request,pk):
    # accepted_requests = request.user.customer.request_set.filter(status='accepted')
    # rejected_requests = request.user.customer.request_set.filter(status='rejected')
    # pending_requests = request.user.customer.request_set.filter(status='pending')
    requested = Request.objects.get(id=pk)
    chats = requested.chat_set.all().order_by('created_at')
    return render(request,'negotiate_expanded.html',{'requested': requested,"chats":chats})
@login_required(login_url='login')
def add_chat_buyer(request):
    if request.method == "POST":
        request_id= request.POST['request_id']
        customer_message = request.POST['customer_message']
        product_cost = request.POST['product_cost']
        pending_chat = Chat()
        pending_chat.customer= request.user.customer
        pending_chat.request = Request.objects.get(id=request_id)
        pending_chat.message= customer_message
        pending_chat.save()
        requested = Request.objects.get(id=request_id)
        requested.cost = product_cost
        requested.save()
        # chats = requested.chat_set.all().order_by('created_at')
        # redirect(f"negotiate_expanded/")
        # return render(request,'negotiate_expanded.html',{'requested': requested,"chats":chats})
        return redirect('my_requests')
        # return 
@login_required(login_url='login')
def add_chat_seller(request):
    if request.method == "POST":
        request_id= request.POST['request_id']
        customer_message = request.POST['customer_message']
        pending_chat = Chat()
        pending_chat.customer= request.user.customer
        pending_chat.request = Request.objects.get(id=request_id)
        pending_chat.message= customer_message
        pending_chat.save()
        requested = Request.objects.get(id=request_id)
        chats = requested.chat_set.all().order_by('created_at')
        return redirect('user_requests')
        # redirect(f"negotiate_expanded/")
        # return render(request,'seller_accepted_expanded.html',{'delivery': requested,"chats":chats})
@login_required(login_url='login')
def success_requests_expanded(request,pk):
    # deliveries = Order.objects.filter(product__seller=request.user.customer)
    # seller_details=deliveries.get(id=pk)
    customer = request.user.customer
    addresses = customer.address_set.all()
    address = addresses[0]
    requested = Request.objects.get(id=pk)
    chats = requested.chat_set.all().order_by('created_at')
    # return redirect(request,'success_requests_expanded.html',{'requested': requested , 'customer': customer, 'address': address, 'chats':chats })
    return render(request,'success_requests_expanded.html',{'requested': requested , 'customer': customer, 'address': address, 'chats':chats })
@login_required(login_url='login')
def products(request):
    products= request.user.customer.product_set.all()
    # products = Product.objects.all()
    return render(request,'products.html',{'products': products})
@login_required(login_url='login')
def user_requests(request):
    # accepted_requests = request.user.customer.request_set.filter(status='accepted')
    # rejected_requests = request.user.customer.request_set.filter(status='rejected')
    pending_requests = Request.objects.filter(status='pending').filter(product__seller=request.user.customer)
    # pending_requests= pending_request.get(status='pending');
    # pending_requests = request.user.customer.request_set.filter(status='pending')
    return render(request,'user_requests.html',{ 'pending_requests': pending_requests})

@login_required(login_url='login')
def seller_accepted_expanded(request,pk):
    # customer = request.delivery.customer
    requests = Request.objects.get(id=pk)
    addresses = requests.customer.address_set.all()
    chats = requests.chat_set.all().order_by('created_at')
    address = addresses[0]
    return render(request,'seller_accepted_expanded.html',{'delivery': requests , 'address': address,'chats':chats })
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
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,password=password)
        #if there is a customer for this user, then only login

        if user is not None and Customer.objects.filter(user=user).exists():
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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            # email = form.cleaned_data['email']
            # if(is_email_present(email)):
                #checking if user already exists
            user=authenticate(password=password,email=email)
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
                    subject = 'Welcome to Acraiders - Your One-Stop Online Sales Portal!'
                    message = f'''Dear {user.first_name},
                    Welcome to Acraiders, your ultimate destination for all your buying and selling needs! We are thrilled to have you join our growing community of users who value convenience, diversity, and seamless transactions.
                    As a member of Acraiders, you now have access to a wide array of products across various categories, all available at your fingertips. Whether you're searching for the latest electronics, timeless books, a new home, or anything in between, Acraiders is your one-stop shop for all things buying and selling.
                    Here are some key highlights of what Acraiders has to offer:
                    1. **Effortless Categorization:** Navigate through our platform effortlessly with our intuitive categorization system, designed to make your shopping experience smooth and enjoyable.
                    2. **Tailored User Accounts:** Whether you're a manager overseeing operations or a customer looking to buy or sell, our platform provides personalized user accounts tailored to your specific needs.
                    3. **Empowering Sellers:** Showcase your items with detailed listings, including high-quality photos, accurate pricing, manufacturing details, and more, to attract potential buyers and maximize your sales potential.
                    4. **Enriched Buyer Experience:** Search for your desired items, negotiate prices, and securely complete transactions online, all within the comfort of your own home.
                    5. **Responsive Management:** Our dedicated managers are here to support you every step of the way, ensuring a seamless experience for both buyers and sellers alike.
                    Your account credentials . Here are your login details:
                    - **User ID:** {user.username}
                    - **Email Address:** {user.email}
                    - **Password:** [Hidden for security purposes]
                    - **Phone Number:** {customer.phone}
                    For your security, we recommend changing your password upon your first login. Please ensure to keep your login credentials confidential to maintain the security of your account.
                    Should you have any questions, require assistance, or simply want to provide feedback, our friendly support team is here to help. Feel free to reach out to us at [Support Email or Contact Number], and we'll be more than happy to assist you.
                    Once again, welcome to Acraiders! We're excited to have you on board and look forward to serving you as you embark on your buying and selling journey with us.
                    Best regards,
                    Team Acraiders'''
                    send_email(user.email,subject, message)
                    return redirect('home')
            else:
                    messages.success(request,("Sorry, couldn't reach server. Please try again...."))
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
            request_id = request.POST['request_id']
            product = Product.objects.get(id=product_id)
            product_price = request.POST['product_price']
            # print(product_price)
            product_qty = request.POST['product_qty']
            print(product_qty)
            seller_email= product.seller.user.email
            #compare integer values of product_qty and product_price
            #cast string to its integer value
            product_qty = int(product_qty)
            product_price = int(product_price)
            if product_qty>product.quantity :
                messages.success(request,("Sorry, that much quantity is not available."))
                return HttpResponse(status=400)
            product.quantity -= product_qty
            if(product.quantity==0):
                product.is_sale = False

            product.save()
            cost = product_price
            print(cost)
            customer = request.user.customer
            customer_email = request.user.email
            pending_order = Order()
            pending_order.product = Product.objects.get(id=product_id)
            pending_order.customer = request.user.customer
            pending_order.quantity = product_qty
            pending_order.cost = cost
            # print(pending_order)
            print('order created')
            pending_order.save()
            delete_request = Request.objects.get(id=request_id)
            delete_request.delete()
            # emailObject1 = EmailMessage(
            #             'Your order is placed'
            #             'Check order details here http://localhost:8000/my_orders',
            #             settings.EMAIL_HOST_USER,
            #             [customer_email],
            #         )
            # emailObject1.send(fail_silently=True)
            # emailObject2 = EmailMessage(
            #             'Your got an order'
            #             'Check order details here http://localhost:8000/my_deliveries',
            #             settings.EMAIL_HOST_USER,
            #             [seller_email],
            #         )
            # emailObject2.send(fail_silently=True)
            #send mail to customer
            send_email(customer_email,'Your order is placed','Check order details here http://localhost:8000/my_orders')
            #send mail to seller
            send_email(seller_email,'Your got an order','Check order details here http://localhost:8000/my_deliveries')
            messages.success(request,("buy successful..."))
            return redirect('orders')
            # we have to return status code 200 to ajax call
            # return json.dumps({'status':'success'})
            # return HttpResponse(status=200)
            print("hi")
        except Exception as e:
            print(e)
            messages.success(request,("buy failure..."))
            return HttpResponse(status=400)
            # redirect()
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
            # create a chat from customer message

            # customer = request.user.customer
            pending_request = Request()
            pending_request.product = Product.objects.get(id=product_id)
            pending_request.customer = request.user.customer
            pending_request.quantity = product_qty
            pending_request.cost = product_cost
            pending_request.customer_message = customer_message
            success_request=pending_request.save()
            added_request_id = pending_request.id
            added_request = Request.objects.get(id=added_request_id)
            pending_chat = Chat()
            pending_chat.customer= request.user.customer
            pending_chat.request = added_request
            pending_chat.message= customer_message
            pending_chat.save()
            # chat = Chat.objects.create(message=customer_message,customer=request.user.customer,request=success_request)
            # product = Product.objects.get(id=product_id)
            # seller = product.seller
            # seller_email = seller.user.email
            # emailObject = EmailMessage(
            #             'You have a new request',
            #             'Please click http://localhost:8000/user_requests',
            #             settings.EMAIL_HOST_USER,
            #             [seller_email],
            #         )
            # emailObject.send(fail_silently=True)
            # messages.success(request,("request successful..."))
            return redirect('my_requests')
        except Exception as e:
            print(e)
            # messages.success(request,("request failure...try again..."))
            return HttpResponse(status=400)
    else:
        return redirect('home')

@login_required(login_url='login')
def accept_request(request):
    if request.method == "POST":
        print('post requested....')
        try:
            request_id = request.POST['request_id']
            print(request_id)
            # seller_message = request.POST['seller_message']
            # print(seller_message)
            pending_request = Request.objects.get(id = request_id)
            print(pending_request)
            
            pending_request.status= 'accepted'
            # pending_request.seller_message= seller_message
            pending_request.save()
            request =  request.POST['request_id']
            # customer_email = request.customer.user.email
            # emailObject = EmailMessage(
            #             'Your request accepted'
            #             'You can buy it now. Please click http://localhost:8000/my_requests',
            #             settings.EMAIL_HOST_USER,
            #             [customer_email],
            #         )
            # emailObject.send(fail_silently=True)
            # messages.success(request,("accepted..."))
            return redirect('user_requests')
        except Exception as e:
            print(e)
            # messages.success(request,("accept failure...try again..."))
            return HttpResponse(status=400)
    else:
        return redirect('home')

@login_required(login_url='login')
def reject_request(request):
    if request.method == "POST":
        print('post requested....')
        try:
            request_id = request.POST['request_id']
            # seller_message = request.POST['seller_message']
            pending_request = Request.objects.get(id = request_id)
            pending_request.status= 'rejected'
            # pending_request.seller_message= seller_message
            pending_request.save()
            request =  request.POST['request_id']
            # customer_email = request.customer.user.email
            # emailObject = EmailMessage(
            #             'Your request rejected'
            #             'You can try again. Please click to see response http://localhost:8000/my_requests',
            #             settings.EMAIL_HOST_USER,
            #             [customer_email],
            #         )
            # emailObject.send(fail_silently=True)
            # messages.success(request,("rejected..."))
            return redirect('user_requests')
        except Exception as e:
            print(e)
            # messages.success(request,("reject failure...try again..."))
            return HttpResponse(status=400)
    else:
        return redirect('home')
    
@login_required(login_url='login')
def issue(request):
    if request.method == "POST":
        print('post requested....')
        try:
            request_id = request.POST['request_id']
            print("1")
            print(request.POST)
            description = request.POST['description']
            print("2")

            pending_request = Order.objects.get(id = request_id)
            print("3")

            pending_issue = Issue()
            print("4")

            pending_issue.request = pending_request
            pending_issue.customer = request.user.customer
            pending_issue.seller = pending_request.product.seller
            pending_issue.description = description
            pending_issue.save()
            messages.success(request,("issue raised..."))
            return redirect('my_requests')
        except Exception as e:
            print(e)
            messages.success(request,("issue failure...try again..."))
            return HttpResponse(status=400)
    else:
        return redirect('home')