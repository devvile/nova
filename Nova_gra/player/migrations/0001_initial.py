<<<<<<< HEAD
# Generated by Django 3.0.6 on 2020-11-25 12:39
=======
# Generated by Django 3.0.6 on 2020-11-25 13:36
>>>>>>> dev

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.CharField(max_length=10)),
                ('nick', models.CharField(max_length=10)),
                ('in_game', models.BooleanField(default=False)),
                ('money', models.IntegerField(default=150)),
                ('position', models.IntegerField(default=0)),
                ('properties', models.CharField(max_length=400, null=True)),
                ('description', models.TextField(max_length=300, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
