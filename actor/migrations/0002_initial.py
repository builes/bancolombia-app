# Generated by Django 5.0.6 on 2024-05-22 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actor', '0001_initial'),
        ('guion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubicacion',
            name='escena',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guion.escena'),
        ),
    ]