# Generated by Django 3.2.8 on 2022-02-25 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_order_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.register'),
        ),
    ]
