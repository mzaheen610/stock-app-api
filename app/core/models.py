"""
Models for the stocks app.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
    )


class UserManager(BaseUserManager):
    """Manager for the users."""

    def create_user(self, email, password=None, **params):
        """Create, save and return a user."""
        if not email:
            raise ValueError("User must have a valid email.")

        user = self.model(email=self.normalize_email(email), **params)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create a admin user. """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Model for a user in the system."""
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'