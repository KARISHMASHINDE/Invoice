from django.db import models
# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    item_name = models.CharField(max_length=100)
    amount = models.IntegerField()

class Invoices(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    invoice_number = models.CharField(max_length=100,unique=True)
    seller = models.CharField(max_length=100)
    buyer = models.CharField(max_length=100)
    status = models.CharField(default="undigitized", max_length=15)
    items = models.ManyToManyField(Item)
    date = models.DateField(auto_now_add=True,null=True)

