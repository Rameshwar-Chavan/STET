from django.shortcuts import render

# Create your views here.


def officer_home(request):
    return render(request, 'admin_home/index_admin.html', {})


def exam_officer_login(request):
    return render(request, 'admin_home/Exam_Officer_Login.html', {})


def exam_investigator_login(request):
    return render(request, 'admin_home/Exam_Investigator_Login.html', {})


def notification(request):
    return render(request, 'admin_home/notifications.html', {})


def timetable(request):
    return render(request, 'admin_home/timetable.html', {})


def results(request):
    return render(request, 'admin_home/result.html')
