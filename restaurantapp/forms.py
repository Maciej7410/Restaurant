from django.forms import (
    CharField, DateField, Form, FloatField, ModelChoiceField, Textarea, ModelForm
)

from restaurantapp.models import Client, Table, OrderDish, Category

# class DishForm(ModelForm):
#
#     class Meta:
#         model = OrderDish
#         exclude = []
#         # fields = '__all__'
#     category = ModelChoiceField(queryset=Category.objects)
#     name = CharField(max_length=20)
#     price = FloatField()
#     description = Textarea()

class DishForm(Form):
    category = ModelChoiceField(queryset=Category.objects)
    name = CharField(max_length=20)
    price = FloatField()
    description = Textarea()

class ReservationForm(Form):
    client = ModelChoiceField(queryset=Client.objects)
    table = ModelChoiceField(queryset=Table.objects)
    order_dish = ModelChoiceField(queryset=OrderDish.objects)
    date_of_reservation = DateField()
    start_time = DateField()
    end_time = DateField()

class CategoryForm(Form):
    name = CharField(max_length=25)