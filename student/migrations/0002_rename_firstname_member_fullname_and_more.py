# Generated by Django 4.2.2 on 2023-07-03 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="member",
            old_name="firstname",
            new_name="fullname",
        ),
        migrations.RenameField(
            model_name="member",
            old_name="lastname",
            new_name="mobile_number",
        ),
    ]
