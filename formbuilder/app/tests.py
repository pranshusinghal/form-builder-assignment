from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from app.models import Form

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.username = 'testuser'
        self.password = 'password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
    
    def test_signup_success(self):
        data = {
            'username': 'newuser@123',
            'password1': 'newpassword@123',
            'password2': 'newpassword@123'
        }
        response = self.client.post(self.signup_url, data)

        self.assertEqual(response.status_code, 302)  # Redirect to the success page
        self.assertTrue(User.objects.filter(username='newuser@123').exists())

    def test_login(self):
        response = self.client.post(self.login_url, {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url, reverse('formlist'))

class FormTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.url = reverse('formcreate')
        self.data = {
           'name': 'Test Name',
        }

    def test_create(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 302)

        obj = Form.objects.first()
        self.assertEqual(obj.name, self.data['name'])

    def test_delete(self):
        obj = Form.objects.create(name='Test Name')
        url = reverse('formdelete', kwargs={'pk': obj.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

        exists = Form.objects.filter(pk=obj.pk).exists()
        self.assertFalse(exists)

