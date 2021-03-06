from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Users', views.UsersViewSet)
urlpatterns = [
    
    
    path('x', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', views.index,name="Index"),
    path('checkotp', views.checkOTP,name="checkOTP"),
]