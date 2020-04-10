from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("buffer stock page")
# Create your views here.
