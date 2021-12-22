from django.db import models


class Notifications(models.Model):

    notification_name = models.CharField(max_length=20)
    notification_str_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True)
    notification_end_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.id


class TimeTable(models.Model):

    exam_name = models.CharField(max_length=20)
    exam_str_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True)
    exam_end_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.id
