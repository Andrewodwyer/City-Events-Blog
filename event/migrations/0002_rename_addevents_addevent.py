# Generated by Django 4.2.15 on 2024-08-23 17:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddEvents',
            new_name='AddEvent',
        ),
    ]
