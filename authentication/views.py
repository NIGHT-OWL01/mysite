from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method=='GET':
        return render(request,'authentication/register.html')
    if request.method=='POST':
        print(request.POST)
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password!=confirm_password:
            messages.warning(request, 'Password not matches!')
            return redirect('/')
        elif User.objects.filter(username=username).exists():
            messages.warning(request, 'Username exists!')
            return redirect('/')
        else:
            messages.success(request,'User created!')
            user=User.objects.create_user(username=username,password=password)
            user.save()
            print(f'user created with username {username} password {password} email {email}')
            return  redirect('login')
            # return HttpResponse('Congratulations! You have successfully registered')
        
        return redirect('/')

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='GET':
        return render(request,'authentication/login.html')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user= authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home page')
        return HttpResponse('wrong credentials ')

def logout(request):
    auth_logout(request)
    return redirect('login')