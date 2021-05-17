from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, password=None, **extra_fields):
        """Create a new user profile"""
        # Add a custom validation error
        if not email:
            raise ValueError('User must have an email address')

        # Create a user from the UserModel
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # Use the set_password method to hash the password
        user.set_password(password)
        # Call save to save the user to the database
        user.save()

        # Always return the user!
        return user

    def create_superuser(self, email, password):
        """Create and save a new superuser with given details"""

        # Use the custom create_user method above to create
        # the user.
        user = self.create_user(email, password)

        # Add the required is_superuser and is_staff properties
        # which must be set to True for superusers
        user.is_superuser = True
        user.is_staff = True
        # Save the user to the database with the new properties
        user.save()

        # Always return the user!
        return user

# Inherit from AbstractBaseUser and PermissionsMixin:
class User(PermissionsMixin, AbstractBaseUser):
    """Database model for users"""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        """Return string representation of the user"""
        return self.email

    def get_auth_token(self):
        """Generates and adds token to User"""
        Token.objects.filter(user=self).delete()
        token = Token.objects.create(user=self)
        self.token = token.key
        self.save()
        return token.key

    def delete_token(self):
        """Removes token from user"""
        Token.objects.filter(user=self).delete()
        self.token = None
        self.save()
        return self