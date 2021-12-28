from django.shortcuts import render
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, validators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from TET_Officers.models import Notifications, TimeTable

# Create your views here.


def officer_home(request):
    return render(request, 'admin_home/index_admin.html', {})


def exam_officer_login(request):
    return render(request, 'admin_home/Exam_Officer_Login.html', {})


def exam_investigator_login(request):
    return render(request, 'admin_home/Exam_Investigator_Login.html', {})


def notification(request):
    all_notifications = Notifications.objects.all()
    if request.method == "POST":
        if request.POST.get('notification_name') and request.POST.get('notification_str_date') and request.POST.get('notification_end_date'):
            insert = Notifications()
            insert.notification_name = request.POST.get('notification_name')
            insert.notification_str_date = request.POST.get(
                'notification_str_date')
            insert.notification_end_date = request.POST.get(
                'notification_end_date')
            insert.save()
            # messages.success(
            #     request, 'New notification is Successfully created !')
            # return render(request, 'admin_home/notifications.html', {})
        else:
            # messages.error(request, 'error while creating new notification')
            return render(request, 'admin_home/notifications.html', {'all_notifications': all_notifications})

    return render(request, 'admin_home/notifications.html', {'all_notifications': all_notifications})


def timetable(request):

    timetable_list = TimeTable.objects.all()
    if request.method == "POST":
        if request.POST.get('exam_name') and request.POST.get('exam_str_date') and request.POST.get('exam_end_date'):
            insert = TimeTable()
            insert.exam_name = request.POST.get('exam_name')
            insert.exam_str_date = request.POST.get(
                'exam_str_date')
            insert.exam_end_date = request.POST.get(
                'exam_end_date')
            insert.save()
            # messages.success(
            #     request, 'New notification is Successfully created !')
            # return render(request, 'admin_home/timetable.html', {})
        else:
            # messages.error(request, 'error while creating new notification')
            return render(request, 'admin_home/timetable.html', {'timetable_list': timetable_list})
    return render(request, 'admin_home/timetable.html', {'timetable_list': timetable_list})


def results(request):
    return render(request, 'admin_home/result.html')


def hallticket(request):
    return render(request, 'admin_home/hallticket.html', {})
