from django.db import models

# Create your models here.
class ShoppingOperation(models.Model):
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    ShoppingOperationUser = models.ForeignKey('ShoppingOperation.ShoppingOperation', on_delete=None)
class pay(models.Model):
    sum1=models.CharField(max_length=100)
    sum2=models.CharField(max_length=100)
    sum=models.IntegerField(max_length=1000)
