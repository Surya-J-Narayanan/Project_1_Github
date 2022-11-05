from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login, logout
# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email ID already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,'user created')
                return redirect('user_login')
        else:
            messages.info(request,'password not matching')
        return redirect('register')
    else:
        return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('/htmlup')
        else:
            messages.info(request,'invalid username or password')
            return redirect('user_login')
    else:
        return render(request,'user_login.html') 

def user_logout(request):
    logout(request)
    return redirect('/htmlup')