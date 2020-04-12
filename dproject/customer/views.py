from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

def index(request):
    if request.method=="POST":
        phone=request.POST.get('phon', '')
        print(phone)
        otp=generateOTP()
        print(otp)
        user=Users(mobile_no=phone,OTP=otp)
        user.save()

        return render(request,'otp.html',{'phone':phone})
        
        

    else:
        return render(request,'index.html')

from rest_framework import viewsets

from .serializers import UsersSerializer
from .models import Users

import math, random 
  
# function to generate OTP 
def generateOTP() : 
  
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
  
   # length of password can be chaged 
   # by changing value in range 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP 
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('name')
    serializer_class = UsersSerializer

# Create your views here.
def checkOTP(request):
        otp=request.POST['otp']
        phon=request.POST['phonehidden']

        print(phon,otp)
        user = Users.objects.filter(mobile_no=phon, OTP=otp)
        if(len(user)==1):
            return HttpResponse("login")
        else:
            return HttpResponse("not login")
