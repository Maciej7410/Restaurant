"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurantapp.views import MenuView, MenuRegistration, ReservationFormView, DishFormView, CategoryFormView
from restaurantapp.models import Reservation, Client, Table, Dish, Category, OrderDish


admin.site.register(Client)
admin.site.register(Table)
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(OrderDish)
admin.site.register(Reservation)



urlpatterns = [
    path('admin/', admin.site.urls),

    path('menu', MenuView.get),
    path('registration', MenuRegistration.as_view(), name='registration'),
    # path('', DishesView.as_view(), name='dish'),
    path('form', ReservationFormView.as_view(), name='reservation_view'),
    path('', DishFormView.as_view(), name='dish_view'),
    path('category', CategoryFormView.as_view()),
]

