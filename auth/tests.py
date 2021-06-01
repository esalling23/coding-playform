from django.test import TestCase
from .models import User

# Create your tests here.
class UserTest(TestCase):

    def create_user(self, email="d@d.com", password="ddddd"):
        return User.objects.create(email=email, password=password)

    def test_user_str(self):
        u = self.create_user()
        self.assertTrue(isinstance(u, User))
        self.assertEqual(u.__str__(), u.email)