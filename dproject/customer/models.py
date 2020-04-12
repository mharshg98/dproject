from django.db import models

# Create your models here.

class Users(models.Model):
    cust_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    lat_long = models.CharField(max_length=30)
    