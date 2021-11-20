from django.shortcuts import render

# Create your views here.
def admin_index(request):
    return render(request, 'admin_home/admin_index.html',{})
def registration(request):
    return render(request, 'admin_home/Admin_Registration.html',{})
def login(request):
    return render(request, 'admin_home/Admin_Login.html',{})