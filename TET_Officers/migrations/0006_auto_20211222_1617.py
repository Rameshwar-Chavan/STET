# Generated by Django 3.1.7 on 2021-12-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TET_Officers', '0005_auto_20211222_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='notification_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='notifications',
            name='notification_str_date',
            field=models.DateField(null=True),
        ),
    ]