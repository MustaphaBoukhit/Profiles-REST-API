from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manager for UserProfile"""
    def create_user(self, email, name, password=None):
        """ Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name) # will create an instance of the model the manager is responsible for
        user.set_password(password)               # will internally hash and store the password to the DB
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ create and save a new superuser with given details """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # as we are overriding the default usrname 
    # field which is normally called username and we're replacing
    # it with out email field. This means whe we are authenticating 
    # users instead of providing a username and password they are 
    # just going to provide their email address and password
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        """ retrieve full name of user """
        return self.name
    
    def get_short_name(self):
        """ retrieve short name of user """
        return self.name

    # it's recommended to django users
    def __str__(self):
        """ return string representation of our user """
        return self.email