from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("This is index page.")

def home(request):
    return HttpResponse('Welcome,This is home page')

def about_us(request):
    return HttpResponse("Welcome,This is About Us page!!")

def contact(request):
    return HttpResponse("Welcome,this is contact page!!")