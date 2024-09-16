# Generated by Django 4.2.15 on 2024-09-16 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_comment_options_addevent_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='addevent',
            name='event_attendees',
            field=models.ManyToManyField(blank=True, related_name='attended_events', to='event.attending'),
        ),
        migrations.AlterField(
            model_name='attending',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='event.addevent'),
        ),
    ]
