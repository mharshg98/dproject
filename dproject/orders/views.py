from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("orders page")
# Create your views here.
