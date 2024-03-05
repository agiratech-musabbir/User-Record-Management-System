from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def index(request):
    return render(request,'index.html')

def registration(request):
    error=""
    if request.method=="POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        ec=request.POST['empcode']
        em=request.POST['email']
        pwd=request.POST['pwd']
        try:
            user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            UserDetail.objects.create(user=user,empcode=ec)
            error="no"
        except:
            error="yes"
        
    return render(request,'registration.html',locals())

def user_login(request):
    error=""
    if request.method=="POST":
        u=request.POST['emailid']
        p=request.POST['password']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            error="no"
        else:
            error="yes"
    return render(request,'user_login.html',locals())

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request,'user_home.html')


def Logout(request):
    logout(request)
    messages.success(request,"You are successfully logout")
    return redirect('index')
    

def profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    user=request.user
    users=UserDetail.objects.get(user=user)
    if request.method=="POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        ec=request.POST['empcode']
        st=request.POST['state']
        cn=request.POST['country']
        con=request.POST['contact']
        gen=request.POST['gender']

        users.user.first_name=fn
        users.user.last_name=ln
        users.empcode=ec
        users.state=st
        users.country=cn
        users.contact=con
        users.gender=gen

        try:
            users.save()
            users.user.save()
            error="no"
        except:
            error="yes"
        
    return render(request,'profile.html',locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    user=request.user

    if request.method== "POST":
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
    
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
        
    return render(request,'change_password.html',locals())

def all_users(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    
    employee=UserDetail.objects.all()

    return render(request,'all_users.html',locals())

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user=User.objects.get(id=pid)
    user.delete()
    return redirect('all_users')


def edit_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    user=request.user
    users=UserDetail.objects.get(id=pid)
    if request.method=="POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        ec=request.POST['empcode']
        st=request.POST['state']
        cn=request.POST['country']
        con=request.POST['contact']
        gen=request.POST['gender']

        users.user.first_name=fn
        users.user.last_name=ln
        users.empcode=ec
        users.state=st
        users.country=cn
        users.contact=con
        users.gender=gen

        try:
            users.save()
            users.user.save()
            error="no"
        except:
            error="yes"
        
    return render(request,'edit_profile.html',locals())


    