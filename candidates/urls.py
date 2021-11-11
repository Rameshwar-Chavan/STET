from django.urls import path

from . import views
from django.core import serializers

app_name = 'candidates'
urlpatterns = [
     path("Applicant_Registration/", views.registration, name="registration"),
     path("Applicant_Login/", views.login, name="login")
]