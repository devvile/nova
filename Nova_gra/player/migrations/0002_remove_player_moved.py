# Generated by Django 3.0.6 on 2020-12-09 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='moved',
        ),
    ]