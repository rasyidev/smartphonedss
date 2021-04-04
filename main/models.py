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

class UserPreference(models.Model):
   user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   performance = models.FloatField()
   price = models.FloatField()
   camera = models.FloatField()
   memory = models.FloatField()
   battery = models.FloatField()
   reputation = models.FloatField()
   is_choosen = models.BooleanField(default=True)

   def __str__(self):
       return f'{self.user}'
   
class Smartphone(models.Model):
   name = models.CharField(max_length=255, unique=True)
   ram = models.FloatField()
   cpu = models.FloatField()
   storage = models.FloatField()
   battery = models.FloatField()
   url = models.CharField(max_length=255)
   img_url = models.CharField(max_length=255)
   main_cam = models.FloatField()
   selfie_cam = models.FloatField()

   def __str__(self):
       return self.name
   

   # price, sold amount, rating
   
class Product(models.Model):
   # pass
   smartphone_model = models.ForeignKey(Smartphone, on_delete=models.CASCADE)
   seller = models.CharField(max_length=255)
   rank = models.IntegerField()
   price = models.IntegerField()
   product_url = models.TextField()

   def __str__(self):
       return self.smartphone_model.name

class Cart(models.Model):
   user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   do_recommendation = models.BooleanField(default=False)

class SmartphoneCart(models.Model):
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
   smartphone = models.ForeignKey(Smartphone, on_delete=models.CASCADE)

class Recomendation(models.Model):
   smartphone_cart = models.ForeignKey(SmartphoneCart, on_delete=models.CASCADE)

class ProductRecommendation(models.Model):
   recommendation = models.ForeignKey(Recomendation, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)