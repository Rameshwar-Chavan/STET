from django.urls import path

from . import views
from django.core import serializers
app_name = 'TET_Officers'
urlpatterns = [
    # path("", views.index, name="index"),
    path("Officer_Dashboard", views.officer_home, name="officer_home"),
    path("EO_Login/", views.exam_officer_login,
         name="EO_Login"),
    path("EIO_Login/", views.exam_investigator_login, name="EIO_Login"),
    path("Notifications/", views.notification, name="Notifications"),
    path("Timetables/", views.timetable, name="Timetables"),
    path("Results/", views.results, name="Results"),

]
