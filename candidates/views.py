from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    return render(request, 'students/Applicant_Registration.html', {})

def login(request):
    return render(request, 'students/Applicant_Login.html', {})
