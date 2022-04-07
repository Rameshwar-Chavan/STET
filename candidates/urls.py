from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.core import serializers

app_name = 'candidates'
urlpatterns = [
    path("Applicant_Registration/", views.registration, name="registration"),
    path("Applicant_Login/", views.user_login, name="login"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path("Applicant_Dashboard/", views.dashboard, name="dashboard"),
    path("Applicant_Profile/", views.profile, name="profile"),
    path("Applicant_Profile/personal/",
         views.applicant_personal, name="personal"),
    path("Applicant_Profile/address/", views.applicant_address, name="address"),
    path("Applicant_Profile/OtherInfo/",
         views.applicant_other_info, name="other"),
    path("Applicant_Profile/academic/",
         views.applicant_academic_info, name="academic"),
    path("Applicant_Profile/documents/",
         views.applicant_documents, name="documents"),

    path("All_Application/", views.all_application, name="All_Application"),
    path("Post_Apply/", views.post_apply, name="Post_Apply"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
