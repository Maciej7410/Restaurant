from django.db.models import (Model,
                              CharField, IntegerField, ForeignKey,
                              DateField, DateTimeField, DO_NOTHING, TextField, FloatField)


class Client(Model):
    name = CharField(max_length=25)
    surname = CharField(max_length=50)
    login = CharField(max_length=50)
    number = IntegerField(max_length=11)
    address = CharField(max_length=40)


class Table(Model):
    name = CharField(max_length=10)
    sits = IntegerField(max_length=10)
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
    client = ForeignKey(Client, on_delete=DO_NOTHING)
    table = ForeignKey(Table, on_delete=DO_NOTHING)
    order_dish = ForeignKey(OrderDish, on_delete=DO_NOTHING)
    date_of_reservation = DateField()
    start_time = DateTimeField()
    end_time = DateTimeField()
    number_of_person = IntegerField(max_length=6)