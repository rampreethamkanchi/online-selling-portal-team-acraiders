from django.test import TestCase
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        response = self.client.post('/login/', {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)
        # Add additional assertions to check if the user is logged in successfully

    def test_login_failure(self):
        response = self.client.post('/login/', {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        # Add additional assertions to check if the login failed

    # Add more test cases for different scenariosfrom django.test import TestCase
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        response = self.client.post('/login/', {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)
        # Add additional assertions to check if the user is logged in successfully

    def test_login_failure(self):
        response = self.client.post('/login/', {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        # Add additional assertions to check if the login failed

    # Add more test cases for different scenarios

    def test_login_redirect(self):
        response = self.client.post('/login/', {'username': self.username, 'password': self.password})
        self.assertRedirects(response, '/dashboard/')  # Assuming successful login redirects to '/dashboard/'

    def test_login_invalid_username(self):
        response = self.client.post('/login/', {'username': 'invaliduser', 'password': self.password})
        self.assertEqual(response.status_code, 401)
        # Add additional assertions to check if the login failed due to invalid username

    def test_login_invalid_password(self):
        response = self.client.post('/login/', {'username': self.username, 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 401)
        # Add additional assertions to check if the login failed due to invalid password