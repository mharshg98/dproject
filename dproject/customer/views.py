from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("customer page")

from rest_framework import viewsets

from .serializers import UsersSerializer
from .models import Users


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('name')
    serializer_class = UsersSerializer

# Create your views here.
