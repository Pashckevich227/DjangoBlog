from django.test import TestCase
from django.urls import reverse


class MyLoginTests(TestCase):

    def setUp(self):
        self.register_url = reverse('signup')
        self.user = {
            'username': 'testusername',
            'email': 'testemail@gmail.com',
            'password1': 'TGBvfred532',
            'password2': 'TGBvfred532'
        }

    def test_registration_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Повтор пароля')
        self.assertTemplateUsed(response, 'signup.html')

    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)
