from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_home_page(self):
        response=self.client.get('/')
        response2=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertEqual(response2.status_code,200)
        self.assertTemplateUsed(response2,'home.html')
    
class SignUpPageTests(TestCase):
    username='maqs'
    email='maqs@gmail.com'
    def test_signup_page_url(self):
        response=self.client.get('/users/signup/')
        response2=self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)
        self.assertEqual(response2.status_code,200)
        self.assertTemplateUsed(response2,'signup.html')
        
    def test_signup_form(self):
        new_user=get_user_model().objects.create_user(self.username,self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,self.email) 
    
