from django.db.models import (Model,
                              CharField, IntegerField, ForeignKey,
                              DateField, DateTimeField, DO_NOTHING, TextField, FloatField, OneToOneField, CASCADE)

from django.contrib.auth.models import User


# dodać pola wymagane i nie wymagane.

class Client(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    phonenumber = CharField(max_length=15)


class Table(Model):
    name = CharField(max_length=10)
    sits = IntegerField()
    description = TextField()


class Category(Model):
    name = CharField(max_length=25)


class Dish(Model):
    category = ForeignKey(Category, on_delete=DO_NOTHING)
    name = CharField(max_length=20)
    price = FloatField()
    description = TextField()


class OrderDish(Model):
    dish = ForeignKey(Dish, on_delete=DO_NOTHING)


class Reservation(Model):
    client = ForeignKey(Client, on_delete=DO_NOTHING, default=None)
    table = ForeignKey(Table, on_delete=DO_NOTHING)
    order_dish = ForeignKey(OrderDish, on_delete=DO_NOTHING)
    date_of_reservation = DateField()
    start_time = DateTimeField()
    end_time = DateTimeField()

