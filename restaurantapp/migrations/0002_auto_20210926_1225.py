# Generated by Django 3.2.7 on 2021-09-26 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='address',
            new_name='emailaddress',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='number',
            new_name='phonenumber',
        ),
    ]
