# Generated by Django 4.0.3 on 2022-04-04 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_number',
            new_name='name',
        ),
    ]
