# Generated by Django 3.0.6 on 2020-05-13 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_match_who_is_playing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='first_player',
        ),
        migrations.RemoveField(
            model_name='match',
            name='forth_player',
        ),
        migrations.RemoveField(
            model_name='match',
            name='second_player',
        ),
        migrations.RemoveField(
            model_name='match',
            name='third_player',
        ),
    ]