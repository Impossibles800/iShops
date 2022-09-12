from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect


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
                send_mail(
                    'iShops-Welcome',
                    'Thankyou for registering in iShops',
                    'marco96wb@gmail.com',
                    ['user.email'],
                    fail_silently=False,
                )
                print("Register successfully")
                return redirect('login_user')
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
        subject = 'iShops-Welcome'
        message = 'You are currently login to iShops'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]

        if user is not None:
            login(request, user)
            send_mail(
                subject,
                message,
                email_from,
                recipient_list,
                fail_silently=False,
            )
            print("Login successfully")
            print(user.email)
            return redirect('products')

        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    send_mail(
        'iShops-Signing Off',
        'You have logout from the iShops',
        'marco96wb@gmail.com',
        ['user.email'],
        fail_silently=False,
    )
    return redirect('products')


def forget_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            send_mail(
                'iShops-Reset Password',
                'You have requested to reset your password'
                'Please click on the link below to reset your password',
                ''
                'marco96wb@gmail.com',
                ['user.email'],
                fail_silently=False,
            )
            print("Email has been sent")
            messages.success(request, "Email has been sent to your email address")
        else:
            messages.error(request, 'Email does not exist')
            return redirect('forget_password')
    return render(request, 'forget_password.html')


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user = User.objects.get(email__exact=email)
        if User.objects.filter(email=email).exists():
            if password == confirm_password:
                user = User.objects.get(email__exact=email)
                user.set_password(password)
                user.save()
                messages.success(request, "Password has been reset")
                print("Password has been reset")
                return redirect('login_user')
            else:
                messages.error(request, 'Password does not match')
                return redirect('reset_password')
        else:
            messages.error(request, 'Email does not exist')
            return redirect('reset_password')

    return render(request, 'reset_password.html')
