from django.test import TestCase
from django.urls import reverse

from accounts.models import Customer
from gstPasswords.models import GenPass


class PasswordViewsTest(TestCase):
    def setUp(self):
        self.user = Customer.objects.create_user(username="alice", password="password123")
        self.other_user = Customer.objects.create_user(username="bob", password="password123")
        self.other_password = GenPass.objects.create(user=self.other_user, site="example.com", passwords="secret")

    def test_home_requires_login(self):
        response = self.client.get(reverse("home_passwords"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_generator_creates_password_for_authenticated_user(self):
        self.client.login(username="alice", password="password123")

        response = self.client.post(reverse("home_passwords"), {"site": " My Site ", "length": 12})

        self.assertEqual(response.status_code, 200)
        generated = response.context["password"]
        self.assertEqual(len(generated), 12)
        self.assertTrue(GenPass.objects.filter(user=self.user, site="My Site").exists())

    def test_user_cannot_delete_someone_elses_password(self):
        self.client.login(username="alice", password="password123")

        response = self.client.post(reverse("deleterecord", args=[self.other_password.id]))

        self.assertEqual(response.status_code, 404)
        self.assertTrue(GenPass.objects.filter(id=self.other_password.id).exists())
