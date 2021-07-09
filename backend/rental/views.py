from django.shortcuts import render
from django.https import HttpResponse

def home(request):
    return HttpResponse("Hey There")
