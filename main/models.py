from django.db import models

# Create your models here.
# class User(models.Model):
#    username = models.CharField(max_length=50)
#    email = models.EmailField(max_length=50)
#    password = models.models.CharField(max_length=255)
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
   email = models.EmailField(_('email address'), unique=True)
   is_staff = models.BooleanField(default=False)
   is_active = models.BooleanField(default=True)
   date_joined = models.DateTimeField(default=timezone.now)
   has_smartphone_preference = models.BooleanField(default=False)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['has_smartphone_preference']

   objects = CustomUserManager()

   def __str__(self):
      return self.email