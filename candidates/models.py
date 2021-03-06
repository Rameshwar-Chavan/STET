from django.db import models
from django.contrib.auth.models import User

class applicant_registration(models.Model):

    applicant_first_name = models.CharField(max_length=20)
    applicant_last_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    mobile = models.BigIntegerField()

    def __str__(self):
        return self.applicant_first_name


class personal_information(models.Model):

    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    d_o_b = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    marital_status = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class address_information(models.Model):

    local_address = models.CharField(max_length=250)
    address_same = models.CharField(max_length=250)
    permanent_address = models.CharField(max_length=250)
    state = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    taluka = models.CharField(max_length=25)
    village = models.CharField(max_length=25)
    pincode = models.IntegerField(max_length=20)

    def __str__(self):
        return self.permanent_address


class other_information(models.Model):

    religion = models.CharField(max_length=20)
    caste = models.CharField(max_length=20)
    person_with_disablity = models.CharField(max_length=20)

    def __str__(self):
        return self.religion


class academic_information(models.Model):

    qualification = models.CharField(max_length=30)
    stream = models.CharField(max_length=30)
    institute_name = models.CharField(max_length=30)
    university_name = models.CharField(max_length=100)
    passing_year = models.IntegerField(max_length=30)
    percentage = models.FloatField(max_length=30)

    def __str__(self):
        return self.qualification

class documents(models.Model):

    ssc_file = models.FileField()
    hsc_file = models.FileField()
    caste_file = models.FileField()
    non_creamy_layer_file = models.FileField()
    passport_photo_file = models.FileField()
    signature_file = models.FileField()

    def __int__(self):
        return self.id