# Generated by Django 5.0.6 on 2024-06-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_wear_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='textile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textile_type', models.CharField(max_length=50)),
                ('textile_color', models.CharField(max_length=50)),
            ],
        ),
    ]
