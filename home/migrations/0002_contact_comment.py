# Generated by Django 3.2.8 on 2021-10-26 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]