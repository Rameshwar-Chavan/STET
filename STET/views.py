from django.http import HttpResponse
from django.shortcuts import render, redirect
from TET_Officers.models import Notifications
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout, validators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .decorators import unauthorized_user, allowed_users


def master(request):
    all_notifications = Notifications.objects.all()
    return render(request, 'base_home.html', {'all_notifications': all_notifications})


def index(request):
    all_notifications = Notifications.objects.all()
    return render(request, 'index.html', {'all_notifications': all_notifications})


def about(request):
    all_notifications = Notifications.objects.all()
    return render(request, 'about.html', {'all_notifications': all_notifications})


def contact(request):
    all_notifications = Notifications.objects.all()
    return render(request, 'contact.html', {'all_notifications': all_notifications})


def forget(request):
    all_notifications = Notifications.objects.all()
    return render(request, 'forget.html', {'all_notifications': all_notifications})


# User Login View

@unauthorized_user
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect('Officer_Dashboard')
        else:
            messages.error(request, 'Incorrect User Name or Password')
            return render(request, 'students:Applicant_Login.html')

    context = {}
    return render(request, 'EIO_Login/', context)


# Logout user View

# def user_logout(request):
#     logout(request)
#     return redirect('students:Applicant_Login')
