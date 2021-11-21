from django.shortcuts import render

# Create your views here.


def officer_home(request):
    return render(request, 'admin_home/admin_index.html', {})


def Exam_Officer_Login(request):
    return render(request, 'admin_home/Exam_Officer_Login.html', {})


def Exam_Investigator_Login(request):
    return render(request, 'admin_home/Exam_Investigator_Login.html', {})
