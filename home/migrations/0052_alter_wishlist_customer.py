# Generated by Django 3.2.8 on 2022-03-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_auto_20220316_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='customer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
