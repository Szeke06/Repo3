# Generated by Django 5.0.1 on 2024-01-28 07:53

import countgame.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countgame', '0005_alter_game_playernr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TEXT', models.CharField(blank=True, max_length=250, null=True)),
                ('TEXT1', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='playernr',
        ),
        migrations.AddField(
            model_name='game',
            name='playersnr',
            field=countgame.models.MySmallIntegerField(default=5, validators=[countgame.models.MySmallIntegerField.validate_range]),
        ),
        migrations.AddField(
            model_name='game',
            name='testg',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countgame.test'),
        ),
    ]
