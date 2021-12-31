from django.shortcuts import render
from candidates.models import applicant_registration, personal_information
from TET_Officers.models import Notifications
from django.contrib import messages
from django.http import HttpResponse


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


def login(request):
    return render(request, 'students/Applicant_Login.html', {})


def dashboard(request):
    return render(request, 'students/Applicant_Dashboard.html', {})


def profile(request):
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
                request, 'Personal Information Successfully Completed !')
            # return render(request, 'students/Applicant_Registration.html', {})
        else:
            messages.error(request, 'Applicant Is Already Registered!')
            return render(request, 'students/Applicant_profile.html', {})

    return render(request, 'students/Applicant_profile.html', {})


def post_apply(request):
    all_notifications = Notifications.objects.all()
    return render(request, 'admin_home/apply.html', {'all_notifications': all_notifications})


def all_application(request):
    all_notifications = Notifications.objects.all()
    return render(request, 'students/all_application.html', {'all_notifications': all_notifications})
