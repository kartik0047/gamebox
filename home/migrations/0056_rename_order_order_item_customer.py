# Generated by Django 3.2.8 on 2022-03-23 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_alter_order_item_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_item',
            old_name='order',
            new_name='customer',
        ),
    ]