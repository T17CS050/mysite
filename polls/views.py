from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request

# Create your views here.

def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")