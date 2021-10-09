from django.contrib import admin
from restaurantapp.models import Reservation, Client, Table, Dish, Category
# Register your models here.
admin.site.register(Client)
admin.site.register(Table)
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Reservation)