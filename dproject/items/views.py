from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("items page")
# Create your views here.
