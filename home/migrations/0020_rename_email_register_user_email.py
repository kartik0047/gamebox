# Generated by Django 3.2.8 on 2022-02-10 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_otp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='email',
            new_name='user_email',
        ),
    ]
