# Generated by Django 4.0.3 on 2022-04-04 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_rename_room_number_room_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='persons',
            new_name='size',
        ),
    ]