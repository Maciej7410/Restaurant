# Generated by Django 3.2.7 on 2021-09-26 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0004_auto_20210926_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='number_of_person',
        ),
    ]
