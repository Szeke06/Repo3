# Generated by Django 5.0.1 on 2024-01-10 11:18

import countgame.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countgame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='playernr',
            field=countgame.models.MySmallIntegerField(validators=[countgame.models.MySmallIntegerField.validate_range]),
        ),
    ]