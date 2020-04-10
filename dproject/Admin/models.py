from django.db import models

# Create your models here.




class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street1 = models.CharField(max_length=50)
    street2 = models.CharField(max_length=50)
    area = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    landmark = models.CharField(max_length=25)
    type = models.CharField(max_length=15)
    def __str__(self):
        return self.address_id

class DeliveryBoy(models.Model):
    delivery_boy_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    lat_long = models.CharField(max_length=30)
    def __str__(self):
        return self.delivery_boy_id

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    units = models.IntegerField()
    price = models.IntegerField()
    catagory = models.CharField(max_length=50 ,default=" ")
    subcategory = models.CharField(max_length=50, default="")
    available_qty = models.IntegerField()
    def __str__(self):
        return self.item_id

class Users(models.Model):
    cust_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    lat_long = models.CharField(max_length=30)
    def __str__(self):
        return self.cust_id



class Vehicle_Info(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_number = models.CharField(max_length=15)
    type = models.CharField(max_length=20)
    user_id = models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE)
    lat_long = models.CharField(max_length=30)
    def __str__(self):
        return self.vehicle_id

class OrderList(models.Model):
    order_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    unit = models.IntegerField()
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.order_id

class UserOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    delivery_location = models.ForeignKey(Address, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    order_list = models.ForeignKey(OrderList, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    def __str__(self):
        return self.order_id





class Order(models.Model):
    customer_id=models.ForeignKey(Users, on_delete=models.CASCADE)
    order_id=models.AutoField(primary_key=True)
    delivery_time=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=30,default="pending")
    item_id=models.ForeignKey(Item, on_delete=models.CASCADE)
    address_id=models.ForeignKey(Address, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    customer_status=models.CharField(max_length=30,default="pending")
    delivery_boy_status=models.CharField(max_length=30,default="pending")
    admin_status=models.CharField(max_length=30,default="pending")

    def __str__(self):
        return self.order_id

class AllotedArea(models.Model):
    user_id=models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE)
    vehicle_id=models.ForeignKey(Vehicle_Info, on_delete=models.CASCADE)
    area_code=models.CharField(max_length=30)

class BufferStock(models.Model):
    item_id=models.ForeignKey(Item,on_delete=models.CASCADE)
    delivery_id=models.ForeignKey(Address, on_delete=models.CASCADE)
    quantity=models.IntegerField()


