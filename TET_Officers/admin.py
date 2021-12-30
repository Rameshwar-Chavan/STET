from django.contrib import admin
from .models import Notifications, TimeTable
# Register your models here.


# @admin.register(Notifications)
# class NotificationsAdmin(admin.ModelAdmin):
#     list_display = ("ID", "Notification Name",
#                     "Start Date", "End Date", "Action")
admin.site.register(Notifications)
admin.site.register(TimeTable)
