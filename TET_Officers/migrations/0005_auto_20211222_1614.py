# Generated by Django 3.1.7 on 2021-12-22 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TET_Officers', '0004_auto_20211222_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='notification_end_date',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='notification_str_date',
        ),
    ]