# Generated by Django 3.2.8 on 2022-03-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_alter_wishlist_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='games',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
