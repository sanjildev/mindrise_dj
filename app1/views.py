from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={
        "body":"Welcome .This is Index Page."
    }
    return render(request,'index.html',context)

def home(request):
    return render(request,'home.html')

def about_us(request):
    return HttpResponse("Welcome,This is About Us page!!")

def contact(request):
    return HttpResponse("Welcome,this is contact page!!")