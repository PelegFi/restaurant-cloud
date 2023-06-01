from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,blank=False,unique=True)
    image=models.TextField()

    class Meta:
        db_table = 'Category'


   

class Dish(models.Model):
    name=models.CharField(max_length=100,blank=False,unique=True)
    price=models.IntegerField(blank=False)
    description=models.TextField(default="")
    image=models.TextField(default="")
    is_gluten_free=models.BooleanField(default=False)
    is_vegeterian=models.BooleanField(default=False)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Dish'

    
