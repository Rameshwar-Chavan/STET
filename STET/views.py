from django.http import HttpResponse
from django.shortcuts import render
from TET_Officers.models import Notifications


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