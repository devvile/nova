# Generated by Django 3.0.5 on 2020-05-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20200501_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='nick',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='player',
            name='parent',
            field=models.CharField(max_length=10),
        ),
    ]
