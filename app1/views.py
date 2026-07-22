from django.shortcuts import render,redirect
from .models import Todolist
from django.http import HttpResponse
# Create your views here.
def home(request):
    task=Todolist.objects.all()
    context={
        "tasks":task
    }
    return render(request,'home.html',context)

def create_task(request):
    if request.method=="POST":
        title=request.POST.get("title")
        description=request.POST.get("description")
        status="status" in request.POST
        Todolist.objects.create(
            title=title,
            description=description,
            status=status
        )
        return redirect('/home')
    return render(request,'create.html')

def delete_task(request,id):
    task=Todolist.objects.get(id=id)
    task.delete()
    return redirect('/home')


def edit_task(request,id):
    task=Todolist.objects.get(id=id)
    context={"task":task}
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        status="status" in request.POST
        task.title=title
        task.description=description
        task.status=status
        task.save()
        return redirect('/home')

    return render(request,'edit.html',context)