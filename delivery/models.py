from django.db import models
from Dishes.models import Dish
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class Items(models.Model):
    dish_id=models.ForeignKey(Dish,on_delete=models.CASCADE)
    cart_id=models.ForeignKey(Cart,on_delete=models.CASCADE)
    amount=models.IntegerField(default=1)

class Delivery(models.Model):
    order_id=models.OneToOneField(Cart,on_delete=models.CASCADE,primary_key=True)
    is_delivered=models.BooleanField(default=False)
    adress=models.CharField(max_length=200,blank=False)
    comments=models.TextField(default="")
    created=models.DateTimeField(auto_now_add=True)