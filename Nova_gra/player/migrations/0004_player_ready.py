# Generated by Django 3.0.6 on 2020-12-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_player_moved'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='ready',
            field=models.BooleanField(default=False),
        ),
    ]
