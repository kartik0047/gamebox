# Generated by Django 3.2.8 on 2022-03-23 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_alter_wishlist_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.register'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='games',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.games'),
        ),
    ]
