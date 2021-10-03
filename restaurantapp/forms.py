from django.forms import (
    CharField, DateField, Form, IntegerField,ModelChoiceField, Textarea
)


from restaurantapp.models import Dish

class DishForm(Form):
    name = CharField(max_length=128)
    price = CharField(max_length=5)
    description = Textarea()
