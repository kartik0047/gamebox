# Generated by Django 3.2.8 on 2022-02-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_rename_sub_total_order_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_item',
            name='image',
            field=models.ImageField(null=True, upload_to='myimage', verbose_name=''),
        ),
    ]
