# Generated by Django 3.2.8 on 2022-03-14 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_alter_order_item_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_item',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.order'),
        ),
    ]
