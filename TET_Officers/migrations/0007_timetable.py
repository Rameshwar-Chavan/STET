# Generated by Django 3.1.7 on 2021-12-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TET_Officers', '0006_auto_20211222_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=20)),
                ('exam_str_date', models.DateField(null=True)),
                ('exam_end_date', models.DateField(null=True)),
            ],
        ),
    ]
