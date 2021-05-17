from django.db import models
from .challenge import Challenge

class TestCase(models.Model):
    """
    Set of input & output for testing challenges

    TestCase >--|- Challenge
    """

    # Solution function input value (could be any valid code value)
    fn_input = models.TextField()
    # Solution function output value (what we expect back from the solution
    # in this test case)
    fn_output = models.TextField()
    # Challenge model relationship
    challenge = models.ForeignKey(
        Challenge, 
        related_name='test_cases',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f"'{self.challenge.title}': {self.fn_input} ==> {self.fn_output}"
