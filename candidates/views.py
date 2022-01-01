from django.shortcuts import render, redirect
from candidates.models import applicant_registration, personal_information
from TET_Officers.models import Notifications
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout, validators

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from STET.decorators import unauthorized_user, allowed_users


def registration(request):
    if request.method == "POST":
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('password') and request.POST.get('mobile'):
            insert = applicant_registration()
            insert.applicant_first_name = request.POST.get('first_name')
            insert.applicant_last_name = request.POST.get('last_name')
            insert.email_id = request.POST.get('email')
            insert.password = request.POST.get('password')
            insert.mobile = request.POST.get('mobile')
            insert.save()
            messages.success(
                request, 'Applicant Registration Successfully Completed !')
            return render(request, 'students/Applicant_Registration.html', {})
        else:
            messages.error(request, 'Applicant Is Already Registered!')
            return render(request, 'students/Applicant_Registration.html', {})

    return render(request, 'students/Applicant_Registration.html', {})


@login_required(login_url='candidates:login')
def dashboard(request):
    return render(request, 'students/Applicant_Dashboard.html', {})


@login_required(login_url='candidates:login')
def profile(request):
    if request.method == "POST":
        if request.POST.get('first_name') and request.POST.get('middle_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('mobile') and request.POST.get('d_o_b') and request.POST.get('gender') and request.POST.get('age') and request.POST.get('marital_status'):
            insert = personal_information()
            insert.first_name = request.POST.get('first_name')
            insert.middle_name = request.POST.get('middle_name')
            insert.last_name = request.POST.get('last_name')
            insert.email_id = request.POST.get('email')
            insert.mobile = request.POST.get('mobile')
            insert.d_o_b = request.POST.get('d_o_b')
            insert.gender = request.POST.get('gender')
            insert.age = request.POST.get('age')
            insert.marital_status = request.POST.get('marital_status')
            insert.save()
            messages.success(
                request, 'Personal Information Successfully Saved!')
            return render(request, 'students/Applicant_profile.html', {})
        else:
            messages.error(request, 'Applicant Is Already Registered!')
            return render(request, 'students/Applicant_profile.html', {})

    return render(request, 'students/Applicant_profile.html', {})


@login_required(login_url='candidates:login')
def post_apply(request):
    all_notifications = Notifications.objects.all()
    return render(request, 'admin_home/apply.html', {'all_notifications': all_notifications})


@login_required(login_url='candidates:login')
def all_application(request):
    all_notifications = Notifications.objects.all()
    return render(request, 'students/all_application.html', {'all_notifications': all_notifications})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('stud_username')
        password = request.POST.get('stud_password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect('candidates:dashboard')
        else:
            messages.error(request, 'Incorrect User Name or Password')
            return render(request, 'students/Applicant_Login.html')

    context = {}
    return render(request, 'students/Applicant_Login.html', context)


# Logout user View
@login_required(login_url='candidates:login')
def user_logout(request):
    logout(request)
    return redirect('candidates:login')
