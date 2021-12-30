from django.contrib import admin
# from django.contrib.admin.decorators
from django.db import models
from django.db.models.base import Model

# Register your models here.
from .models import applicant_registration


# @admin.register(applicant_registration)
# class AdminApplicants(admin.ModelAdmin):
#     list_display = ('ID', 'User Name', 'Mobile No', 'Email Id')
admin.site.register(applicant_registration)
