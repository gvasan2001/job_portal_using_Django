# Generated by Django 5.1.2 on 2024-10-25 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_rename_applyer_company_schedule_company_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userapply',
            old_name='dob',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='userapply',
            old_name='pincode',
            new_name='jobrole',
        ),
    ]