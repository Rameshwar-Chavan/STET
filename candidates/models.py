from django.db import models


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
