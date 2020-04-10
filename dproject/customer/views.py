from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("customer page")
# Create your views here.
