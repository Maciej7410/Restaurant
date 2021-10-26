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

from restaurantapp.views import (MainView, SignInView, RegisterUser, DishView, CategoryView,
                                 LogOutUser, MenuView, ReservationView,MenuReservationOrderView,
                                 CategoryOrderView, DishOrderView, OrderView)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', MenuView.as_view(), name='menu_view'),
    # path('menu/<reservation_get_id>', ReservationIdSend.as_view(), name='menu_view'),
    path('category/<id_category>/', CategoryView.as_view(), name='category_view'),
    path('category/dishes/<id_category>/<id_dish>/', DishView.as_view(), name='dish_view'),
    path('category/dishes/<id_category>/<id_dish>/<id_reservation>', OrderView.as_view(), name='order_view'),
    path('order/', OrderView.as_view(), name='order_view'),
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('', MainView.as_view(), name='main'),
    path('logout/', LogOutUser.as_view(), name='logout'),
    path('main/', MainView.as_view(), name='main'),
    path('login/', SignInView.as_view(), name='signin'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('menu_order/<id_reservation>', MenuReservationOrderView.as_view(), name='menu_reservation_order'),
    path('category_order/<id_reservation>/<id_category>', CategoryOrderView.as_view(), name='category_order_view'),
    path('dishes_order/<id_reservation>/<id_category>/<id_dish>', DishOrderView.as_view(), name='dish_order_view'),

]
