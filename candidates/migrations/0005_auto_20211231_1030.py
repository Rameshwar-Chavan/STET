# Generated by Django 3.1.4 on 2021-12-31 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='personal_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('d_o_b', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('marital_status', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
