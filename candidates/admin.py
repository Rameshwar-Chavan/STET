from django.contrib import admin
# from django.contrib.admin.decorators
from django.db import models
from django.db.models.base import Model
from candidates.models import applicant_registration, personal_information, address_information, other_information, academic_information, documents
# Register your models here.



# @admin.register(applicant_registration)
# class AdminApplicants(admin.ModelAdmin):
#     list_display = ('ID', 'User Name', 'Mobile No', 'Email Id')
admin.site.register(applicant_registration)
admin.site.register(personal_information)
admin.site.register(other_information)
admin.site.register(address_information)
admin.site.register(academic_information)
admin.site.register(documents)