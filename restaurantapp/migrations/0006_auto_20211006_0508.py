# Generated by Django 3.2.7 on 2021-10-06 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0005_remove_reservation_number_of_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
