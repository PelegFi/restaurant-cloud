from django.db import models

# Create your models here.
class my_User(models.Model):
    username=models.CharField(max_length=20,unique=True,null=False)
    password=models.CharField(max_length=20,unique=True,null=False)
    first_name=models.CharField(null=False,max_length=20)
    last_name=models.CharField(null=False,max_length=20)
    is_staff=models.BooleanField(default=False)
    email=models.EmailField(null=False,default="")
