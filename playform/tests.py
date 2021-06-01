from django.test import TestCase as DjangoTestCase
from django.contrib.auth import get_user_model

from .models.attempt import Attempt
from .models.challenge import Challenge
from .models.test_case import TestCase

# Create your tests here.
class ChallengeTest(DjangoTestCase):
    """Tests the Challenge model"""
    def create_challenge(self, title="Challenge Test", description="Challenge description..."):
        return Challenge.objects.create(title=title, description=description)

    def test_challenge_model_str(self):
        """Tests challenge model __str__ method"""
        c = self.create_challenge()
        self.assertTrue(isinstance(c, Challenge))
        self.assertEqual(c.__str__(), c.title)

class TestCaseTest(DjangoTestCase):
    """Tests the TestCase model"""
    def create_test_case(self, fn_input=[1, 2, 3], fn_output=1):
        the_challenge = ChallengeTest().create_challenge()
        return TestCase.objects.create(fn_input=fn_input, fn_output=fn_output, challenge_id=the_challenge.id)
    
    def test_test_case_model_str(self):
        c = self.create_test_case()
        self.assertTrue(isinstance(c, TestCase))
        self.assertEqual(c.__str__(), f"'{c.challenge.title}': {c.fn_input} ==> {c.fn_output}")

class AttemptTest(DjangoTestCase):
    """Tests the Attempt model"""
    def create_attempt(self, user_solution='x = 1'):
        the_challenge = ChallengeTest().create_challenge()
        the_user = get_user_model().objects.create(email="d@g.com", password="ddddd")
        return Attempt.objects.create(owner=the_user, challenge=the_challenge, user_solution=user_solution)

    def test_attempt_model_str(self):
        c = self.create_attempt()
        self.assertTrue(isinstance(c, Attempt))
        self.assertEqual(c.__str__(), f"Attempt #{c.id}")