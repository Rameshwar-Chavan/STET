from django.urls import path

from . import views
from django.core import serializers

app_name = 'candidates'
urlpatterns = [
    path("Applicant_Registration/", views.registration, name="registration"),
    path("Applicant_Login/", views.login, name="login"),
    path("Applicant_Dashboard/", views.dashboard, name="dashboard"),
    path("Applicant_profile/", views.profile, name="profile"),
    path("All_Application/", views.all_application, name="All_Application"),
    path("Post_Apply/", views.post_apply, name="Post_Apply"),
]
