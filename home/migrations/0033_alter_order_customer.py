# Generated by Django 3.2.8 on 2022-02-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_alter_order_item_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]