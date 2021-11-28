from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Location, Category

# Create your views here.
def welcome(request):
    return HttpResponse('Photography web app')
