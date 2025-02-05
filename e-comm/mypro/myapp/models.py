from django.db import models

# Create your models here.
class Product(models.Model):
    category=models.CharField(max_length=10)
    pname=models.CharField(max_length=10)
    rate=models.IntegerField()
    image=models.FileField(upload_to="file")
class Stock(models.Model):
    qty=models.IntegerField()
    pid=models.ForeignKey(Product,on_delete=models.CASCADE)
class Reg(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    addr=models.TextField()
    loc=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phno=models.BigIntegerField()
class Login(models.Model):
    
    
    uname=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    utype=models.CharField(max_length=20)
    uid=models.ForeignKey(Reg,on_delete=models.CASCADE)

class cart(models.Model):
    date=models.DateField()
    uid=models.ForeignKey(Reg,models.CASCADE)
    pid=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    total=models.IntegerField()

class order_master(models.Model):
    uid=models.ForeignKey(Reg,on_delete=models.CASCADE)
    date=models.DateField()
    gtotal=models.IntegerField()

class order_child(models.Model):
    oid=models.ForeignKey(order_master,on_delete=models.CASCADE)
    pid=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    total=models.IntegerField()
    status=models.CharField(max_length=10)
    