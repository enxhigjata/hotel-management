# Generated by Django 4.0.3 on 2022-04-04 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='size',
            new_name='persons',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='name',
            new_name='room_number',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='name',
        ),
    ]