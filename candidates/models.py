from django.db import models


class applicant_registration(models.Model):

    applicant_first_name = models.CharField(max_length=20)
    applicant_last_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    mobile = models.BigIntegerField()

    def __str__(self):
        return self.applicant_first_name


class Profile(models.Model):

    candidate_first_name = models.CharField(max_length=20)
    candidate_last_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    mobile = models.BigIntegerField()

    def __str__(self):
        return self.applicant_first_name
