# Generated by Django 5.1.5 on 2025-01-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blacklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklist',
            name='ip_address',
            field=models.GenericIPAddressField(unique=True),
        ),
    ]
