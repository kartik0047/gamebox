# Generated by Django 3.2.8 on 2022-03-28 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_auto_20220328_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
