from django.shortcuts import render
from django.http import HttpResponse

def greet(request):
    res=render(request,'learnig/test.html',)
    return res





# Create your views here.
