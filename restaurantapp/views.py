from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from restaurantapp.forms import LoginForm
from django.views.generic import CreateView
from restaurantapp.forms import RegisterView
from django.urls import reverse_lazy

import logging

from restaurantapp.models import Category, Dish, Reservation
from datetime import timedelta
import time

logger = logging.getLogger(__name__)


class ReservationView(View):
    def get(self, request):
        return render(
            request,
            template_name='Reservation.html',

        )

    def post(self, request):
        result = ""
        update = True
        date_post = request.POST.get('date', 'none')
        time_post = request.POST.get('time', 'none')
        date_time = date_post + ' ' + time_post
        date_time_join = time.strptime(str(date_time), "%Y-%m-%d %H:%M")
        end_time = time.strptime(time_post, "%H:%M").tm_hour + 1
        # end_time = time.strptime(time_post, "%H:%M").tm_hour + 1
        table_post = int(request.POST.get('table', 'none'))
        registration_db = Reservation.objects.all()

        user_active = int(request.user.id)
        logger.warn(user_active)
        for start_date in registration_db:
            date_time_db = str(start_date.date_of_reservation) + ' ' + str(start_date.end_time)
            date_time_join_db = time.strptime(date_time_db, '%Y-%m-%d %H:%M:%S')
            if date_time_join_db.tm_hour == date_time_join.tm_hour and \
                    date_time_join_db.tm_min == date_time_join.tm_min and \
                    date_time_join_db.tm_year == date_time_join.tm_year and \
                    date_time_join_db.tm_mon == date_time_join.tm_mon and \
                    date_time_join_db.tm_mday == date_time_join.tm_mday and \
                    table_post == start_date.table_id:
                result = "Unsaved"
                update = False
        if update == True:
            deadline = Reservation(date_of_reservation=date_post, end_time=time_post,
                                   table_id=table_post, client_id=user_active, start_time=time_post)
            deadline.save()
            result = "Saved"

        return render(
            request,
            template_name='Reservation.html',
            context={
                'result': result,
                'update': update,
                'start_date': date_post,
                'start_time': time_post,
                'end_time': end_time,
                'table_post': table_post,
                'user_active': user_active
            }
        )


class MenuView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request,
                      template_name='Menu.html',
                      context={'categories': categories
                               })


class CategoryView(View):
    def get(self, request, id_category):
        selected_category = Category.objects.get(pk=id_category)
        dish_received = Dish.objects.filter(category=selected_category)
        categories = Category.objects.all()
        return render(request,
                      template_name='Category.html',
                      context={'selected_category': selected_category,
                               'dish_received': dish_received,
                               'categories': categories,
                               'id_categories': id_category})


class DishView(View):
    def get(self, request, id_category, id_dish):
        selected_category = Category.objects.get(pk=id_category)
        dish_received = Dish.objects.filter(category=selected_category)
        categories = Category.objects.all()
        dishes = Dish.objects.get(pk=id_dish)
        categories = Category.objects.all()
        id_user = int(request.user.id)
        # reservation_user = Reservation.objects.all()
        reservation_user = Reservation.objects.filter(client__id=id_user)
        user_name = request.user.username

        return render(request,
                      template_name="Dishes.html",
                      context={'dishes': dishes,
                               'categories': categories,
                               'id_categories': id_category,
                               'id_dish': id_dish,
                               'selected_category': selected_category,
                               'dish_received': dish_received,
                               'reservation_user': reservation_user,
                               'id_user': id_user,
                               'username': user_name
                               })


class OrderView(View):
    def get(self, request, id_category, id_dish, id_reservation):
        reservation = Reservation.objects.get(id=id_reservation)
        dish = Dish.objects.get(id=id_dish)
        reservation.dishes.add(dish)

        reservation.save()
        # list of ordered dishes
        my_ordered_dishes = reservation.dishes.all()
        # delete item

        # total Price
        total = 0
        for dish in reservation.dishes.all():
            total += dish.price
        # DishView
        selected_category = Category.objects.get(pk=id_category)
        dish_received = Dish.objects.filter(category=selected_category)
        categories = Category.objects.all()
        dishes = Dish.objects.get(pk=id_dish)
        categories = Category.objects.all()
        id_user = int(request.user.id)

        # End DishView

        return render(request,
                      template_name="Ordered.html",
                      context={'dishes': dishes,
                               'categories': categories,
                               'id_categories': id_category,
                               'id_dish': id_dish,
                               'selected_category': selected_category,
                               'dish_received': dish_received,
                               'reservation_user': id_reservation,
                               'id_user': id_user,
                               'ordered': my_ordered_dishes,
                               'total': total,
                               })


class MainView(View):
    def get(self, request):
        return render(
            request,
            template_name='Main.html',
            context={'main': ''}
        )


class SignInView(LoginView):
    template_name = 'Signin.html'
    form_class = LoginForm
    success_url = reverse_lazy('admin')


class RegisterUser(CreateView):
    template_name = 'Register.html'
    form_class = RegisterView
    success_url = reverse_lazy('main')


class LogOutUser(LogoutView):
    template_name = 'Logout.html'

    def log_out(self, request):
        logout(request)
