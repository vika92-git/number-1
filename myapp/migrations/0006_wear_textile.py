# Generated by Django 5.0.6 on 2024-06-16 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_textile'),
    ]

    operations = [
        migrations.AddField(
            model_name='wear',
            name='textile',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.textile'),
        ),
    ]
