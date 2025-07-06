from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.
def index(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your Password and Confirm Password is not Same !!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect(login)

    return render(request,"index2.html")


def service(request):
    return render(request,"service.html")

def fees(request):
    return render(request,"fee.html")

def about(request):
    return render(request,"about.html")

def contactus(request):
    return render(request,"contact.html")

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request,"login.html")
def dashboard(request):
    return render(request,'dashboard.html')