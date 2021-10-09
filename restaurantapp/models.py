from django.db.models import (Model,
                              CharField, IntegerField, ForeignKey,
                              DateField, DateTimeField, DO_NOTHING, TextField, FloatField,
                              OneToOneField, CASCADE, DecimalField)

from django.contrib.auth.models import User




class Client(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    phonenumber = CharField(max_length=15)


class Table(Model):
    name = CharField(max_length=10)
    sits = IntegerField()
    description = TextField()


class Category(Model):
    name = CharField(max_length=25)
    def __str__(self):
        return self.name


class Dish(Model):
    category = ForeignKey(Category, on_delete=DO_NOTHING)
    name = CharField(max_length=40)
    price = DecimalField(max_digits=5, decimal_places=2)
    description = TextField(blank=True)
    def __str__(self):
        return self.name

class OrderList(Model):
    name = CharField(max_length=40)
    price = DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name
class OrderDish(Model):
    dish = ForeignKey(Dish, on_delete=DO_NOTHING)



class Reservation(Model):
    client = ForeignKey(Client, on_delete=DO_NOTHING, default=None)
    table = ForeignKey(Table, on_delete=DO_NOTHING)
    order_dish = ForeignKey(OrderDish, on_delete=DO_NOTHING)
    date_of_reservation = DateField()
    start_time = DateTimeField()
    end_time = DateTimeField()

