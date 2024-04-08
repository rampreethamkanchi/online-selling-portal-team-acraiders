from store.models import User,Customer,Manager,Address
from django.test import TestCase,Client
from .urls import reverse

class TestLogin(TestCase):
    def setUp(self):
        # Create test users
        # Superuser
        self.superuser = User.objects.create_superuser(username='acraiders', email='acraiders@gmail.com', password='acr@2004', first_name='acraiders', last_name='owner')
        self.client = Client()
        self.url = reverse('login')
        # Customers
        self.customer1 = User.objects.create_user(username='jaswanth', email='jaswanth@gmail.com', password='xyz@2004', first_name='Jaswanth', last_name='Mantri')
        self.customer2 = User.objects.create_user(username='varun', email='varun@gmail.com', password='xyz@2004', first_name='Varun', last_name='Mupparaju')
        self.customer3 = User.objects.create_user(username='nishnath', email='nishnath@gmail.com', password='xyz@2004', first_name='Nishnath', last_name='Parimi')

        # Managers
        self.manager1 = User.objects.create_user(username='rampreetham', email='rampreetham@gmail.com', password='xyz@2004', first_name='Rampreetham', last_name='Kanchi')
        self.manager2 = User.objects.create_user(username='karthikeya', email='karthikeya@gmail.com', password='xyz@2004', first_name='Karthikeya', last_name='Poondla')

        from store.models import Customer, Manager, Address
        # Create customers
        Customer.objects.create(user=self.customer1, phone='9032256780')
        Customer.objects.create(user=self.customer2, phone='9032256781')
        Customer.objects.create(user=self.customer3, phone='9032256782')

        # Create addresses for customers
        Address.objects.create(customer=Customer.objects.get(user=self.customer1), city='Nellore', state='Andhra Pradesh', pincode='500072', street='Kanchi Nagar', house_no='12/543/1')
        Address.objects.create(customer=Customer.objects.get(user=self.customer2), city='Hyderabad', state='Telangana', pincode='500073', street='Mupparaju Nagar', house_no='12/543/2')
        Address.objects.create(customer=Customer.objects.get(user=self.customer3), city='Nellore', state='Andhra Pradesh', pincode='500072', street='Parimi Nagar', house_no='12/543/3')

        # Create managers
        Manager.objects.create(user=self.manager1, gender='male', phone='9032256785', city='Nellore', state='Andhra Pradesh', pincode='500072', street='Kanchi Nagar', dob='2004-04-20', locality='Kanchi Nagar')
        Manager.objects.create(user=self.manager2, gender='male', phone='9032256786', city='Hyderabad', state='Telangana', pincode='500073', street='Poondla Nagar', dob='2004-04-21', locality='Poondla Nagar', house_no='12/543/1')

    def test_customer_login(self):
        # Test customer login
        response = self.client.post(self.url, {'email': 'jaswanth@gmail.com', 'password': 'xyz@2004'}, follow=True)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(response.context['user'].is_authenticated)

    def test_manager_login(self):
        # Test manager login
        response = self.client.post(self.url, {'email': 'rampreetham@gmail.com', 'password': 'xyz@2004'}, follow=True)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(response.context['user'].is_authenticated)

    def test_superuser_login(self):
        # Test superuser login
        response = self.client.post(self.url, {'email': 'acraiders@gmail.com', 'password': 'acr@2004'}, follow=True)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(response.context['user'].is_authenticated)
