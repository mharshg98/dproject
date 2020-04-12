from rest_framework import serializers

from .models import Users

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('cust_id', 'name','mobile_no','address','lat_long')