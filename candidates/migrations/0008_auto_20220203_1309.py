# Generated by Django 3.1.4 on 2022-02-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0007_auto_20220202_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='caste_file',
            field=models.FileField(upload_to='./files/'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='hsc_file',
            field=models.FileField(upload_to='./files/'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='non_creamy_layer_file',
            field=models.FileField(upload_to='./files/'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='passport_photo_file',
            field=models.FileField(upload_to='./files/'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='signature_file',
            field=models.FileField(upload_to='./files/'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='ssc_file',
            field=models.FileField(upload_to='./files/'),
        ),
    ]