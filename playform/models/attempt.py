from django.db import models
from django.contrib.auth import get_user_model

from .challenge import Challenge

class Attempt(models.Model):
    # Ownership field - relationship to `User` model
    owner = models.ForeignKey(
        get_user_model(),
        related_name='challenge_attempts',
        on_delete=models.CASCADE,
    )
    # Relationship to `Challenge` model
    challenge = models.ForeignKey(
        Challenge,
        related_name='attempts',
        on_delete=models.CASCADE,
    )
    # User's solution so far (the last time they ran it)
    user_solution = models.TextField()
    # Number of times user's solution has passed or failed
    # the provided tests for the associated challenge
    passes = models.IntegerField()
    failures = models.IntegerField()