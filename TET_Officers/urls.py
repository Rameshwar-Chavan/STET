from django.urls import path

from . import views
from django.core import serializers
app_name = 'TET_Officers'
urlpatterns = [
    # path("", views.index, name="index"),
    path("TET_Officers/admin_home", views.admin_index, name="admin_index"),
]
