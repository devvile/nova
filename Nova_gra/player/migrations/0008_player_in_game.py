# Generated by Django 3.0.6 on 2020-05-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0007_remove_player_in_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='in_game',
            field=models.BooleanField(default=False),
        ),
    ]