from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    data= Test.objects.all()
    return render(request, "main/home.html",{"data": data})


def post(request):
    if request.method=="POST":
        task= request.POST["task"]
        time= request.POST["time"]

# burda 1ci yazilan Testdeki addi 2ci yuxarida yazdigimiz
        data= Test(task=task, time=time)  
        data.save()  

    return redirect("home")


# def delete(request):

# # database dan hamisini silir 
#     Test.objects.all().delete()
#     return redirect("home")

def delete(request,id):
    data=Test.objects.get(id=id)
    data.delete()
    return redirect("home")