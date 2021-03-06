# Generated by Django 4.0.3 on 2022-04-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_rename_name_room_room_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant_Bar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('picture', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'restaurant',
                'verbose_name_plural': 'restaurants',
            },
        ),
    ]
