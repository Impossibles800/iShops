from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'products.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not User.objects.filter(email=email).exists():
            if password == confirm_password:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Register successfully")
                print("Register successfully")
                return redirect('login')
            else:
                messages.error(request, 'Password does not match')
                print('Password does not match')
                return redirect('register')
        else:
            messages.error(request, 'Email already exists')
            print('Email already exists')
            return redirect('register')
    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Login successfully")
            return redirect('home')

        else:
            messages.error(request, "Invalid email or password")
    return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('products')
