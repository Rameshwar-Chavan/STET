from django.shortcuts import render, redirect
from candidates.models import applicant_registration, personal_information, address_information, other_information, academic_information, documents
from TET_Officers.models import Notifications
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout, validators

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from STET.decorators import unauthorized_user, allowed_users


def registration(request):
    all_notifications = Notifications.objects.all()
    context = {'all_notifications': all_notifications}
    if request.method == "POST":
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('password') and request.POST.get('mobile'):
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            mobile = request.POST['mobile']

            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            print("User Created")
            messages.success(
                request, 'Applicant Registration Successfully Completed !')
            return render(request, 'students/Applicant_Registration.html', {})
        else:
            messages.error(request, 'Applicant Is Already Registered!')
            return render(request, 'students/Applicant_Registration.html', {})

    return render(request, 'students/Applicant_Registration.html', context)


@login_required(login_url='candidates:login')
def applicant_personal(request):
    print("This is a method::",request.method)
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
            messages.success(request, 'Personal Information Successfully Saved!')
            return render(request, 'students/applicant_personal.html', {})
        else:
            messages.error(request, 'Applicant Is Already Registered!')
            return render(request, 'students/applicant_personal.html', {})
    else:
        messages.error(request, 'Method Is GET!')
        return render(request, 'students/applicant_personal.html', {})

    return render(request, 'students/applicant_personal.html', {})


@login_required(login_url='candidates:login')
def applicant_address(request):
    if request.method == "POST":
        if request.POST.get('local_address') and request.POST.get('address_same') and request.POST.get('permanent_address') and request.POST.get('state') and request.POST.get('district') and request.POST.get('taluka') and request.POST.get('village') and request.POST.get('pincode'):
            insert = address_information()
            insert.local_address = request.POST.get('local_address')
            insert.address_same = request.POST.get('address_same')
            insert.permanent_address = request.POST.get('permanent_address')
            insert.state = request.POST.get('state')
            insert.district = request.POST.get('district')
            insert.taluka = request.POST.get('taluka')
            insert.village = request.POST.get('village')
            insert.pincode = request.POST.get('pincode')
            insert.save()
            messages.success(request, 'Address Information Successfully Saved!')
            return render(request, 'students/applicant_address.html', {})

    return render(request, 'students/applicant_address.html', {})


@login_required(login_url='candidates:login')
def applicant_other_info(request):
    if request.method == "POST":
        if request.POST.get('religion') and request.POST.get('caste') and request.POST.get('pwd'):
            insert = other_information()
            insert.religion = request.POST.get('religion')
            insert.caste = request.POST.get('caste')
            insert.person_with_disablity = request.POST.get('pwd')
            insert.save()
            messages.success(request, 'Other Information Successfully Saved!')
            return render(request, 'students/applicant_other_info.html', {})

    return render(request, 'students/applicant_other_info.html', {})


@login_required(login_url='candidates:login')
def applicant_academic_info(request):
    if request.method == "POST":
        if request.POST.get('qualification') and request.POST.get('stream') and request.POST.get('institute name') and request.POST.get('university') and request.POST.get('passing_year') and request.POST.get('Percentage'):
            insert = academic_information()
            insert.qualification = request.POST.get('qualification')
            insert.stream = request.POST.get('stream')
            insert.institute_name = request.POST.get('institute name')
            insert.university_name = request.POST.get('university')
            insert.passing_year = request.POST.get('passing_year')
            insert.percentage = request.POST.get('Percentage')
            insert.save()
            messages.success(request, 'Academic Information Successfully Saved!')
            return render(request, 'students/applicant_academic_info.html', {})

    return render(request, 'students/applicant_academic_info.html')


@login_required(login_url='candidates:login')
def applicant_documents(request):
    if request.method == "POST":
            ssc_file = request.FILES.getlist('ssc_file')
            hsc_file = request.FILES.getlist('hsc_file')
            caste_file = request.FILES.getlist('caste_file')
            non_creamy_layer_file = request.FILES.getlist('non_creamy_layer_file')
            passport_photo_file = request.FILES.getlist('passport_photo_file')
            signature_file = request.FILES.getlist('signature_file')
            documents(ssc_file=ssc_file, hsc_file=hsc_file, caste_file=caste_file, non_creamy_layer_file= non_creamy_layer_file, passport_photo_file=passport_photo_file, signature_file=signature_file).save()
            messages.success(request, 'Documents Uploaded Successfully !')
            return render(request, 'students/applicant_documents.html', {})
    else:
         messages.error(request, 'error !')
         return render(request, 'students/applicant_documents.html', {})

    return render(request, 'students/applicant_documents.html', {})


@login_required(login_url='candidates:login')
def dashboard(request):
    return render(request, 'students/Applicant_Dashboard.html', {})


@login_required(login_url='candidates:login')
def profile(request):
    all_notifications = Notifications.objects.all()
    return render(request, 'students/Applicant_profile.html', {'all_notifications': all_notifications})


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
    all_notifications = Notifications.objects.all()
    context = {'all_notifications': all_notifications}
    return render(request, 'students/Applicant_Login.html', context)


# Logout user View
@login_required(login_url='candidates:login')
def user_logout(request):
    logout(request)
    return redirect('candidates:login')
