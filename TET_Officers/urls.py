from django.urls import path

from . import views
from django.core import serializers
app_name = 'TET_Officers'
urlpatterns = [
    # path("", views.index, name="index"),
    path("Officer_Dashboard", views.officer_home, name="officer_home"),
    path("EO_Login/", views.Exam_Officer_Login,
         name="EO_Login"),
    path("EIO_Login/", views.Exam_Investigator_Login, name="EIO_Login")
]
