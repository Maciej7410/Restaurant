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

from restaurantapp.views import MainView, SignInView, RegisterUser
from restaurantapp.views import menu_view, dish_view, category_view, OrderView, ReservationView

from restaurantapp.models import Reservation, Client, Table, Dish, Category, OrderDish

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu', menu_view, name='menu_view'),
    path('category/<id>/', category_view, name='category_view'),
    path('dishes/<id>/', dish_view, name='dish_view'),
    path('order/<id>/', OrderView, name='order_view'),
    path('reservation', ReservationView.as_view(), name='reservation'),
    path('', MainView.as_view(), name='main'),
    path('login/', SignInView.as_view(), name='signin'),
    path('register/', RegisterUser.as_view(), name='register')
]
