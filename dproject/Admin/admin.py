from django.contrib import admin

# Register your models here.

from . models import Address, Item,BufferStock , DeliveryBoy ,AllotedArea,OrderList,Order,UserOrder,Vehicle_Info
admin.site.register(Address)
admin.site.register(Item)
admin.site.register(DeliveryBoy)
admin.site.register(AllotedArea)
admin.site.register(OrderList)
admin.site.register(Order)
admin.site.register(UserOrder)
admin.site.register(Vehicle_Info)
admin.site.register(BufferStock)