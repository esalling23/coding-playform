from django.contrib import admin

# Register your models here.
from .models.attempt import Attempt
from .models.challenge import Challenge
from .models.test_case import TestCase

admin.site.register(Attempt)
admin.site.register(Challenge)
admin.site.register(TestCase)
