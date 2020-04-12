from django.db import models

# Create your models here.
class DeliveryBoy(models.Model):
    delivery_boy_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    lat_long = models.CharField(max_length=30)
    def __str__(self):
        return self.delivery_boy_id