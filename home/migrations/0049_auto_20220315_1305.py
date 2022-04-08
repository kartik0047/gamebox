# Generated by Django 3.2.8 on 2022-03-15 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_rename_game_wishlist_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='game',
            new_name='games',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.register'),
        ),
    ]