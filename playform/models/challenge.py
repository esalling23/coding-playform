from django.db import models

class Challenge(models.Model):
    """A coding challenge users can attempt"""
    # Challenge title and description fields will be filled out
    # by the user who creates this challenge
    title = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return self.title
