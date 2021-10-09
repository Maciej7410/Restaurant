from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from restaurantapp.forms import LoginForm
from django.views.generic import CreateView
from restaurantapp.forms import RegisterView
from django.urls import reverse_lazy
from restaurantapp.models import Table, Category, Dish, Reservation, OrderDish, OrderList
from restaurantapp.models import Table, Category, Dish, Reservation
from datetime import timedelta
import time


class ReservationView(View):
    def get(self, request):
        return render(
            request,
            template_name='Reservation.html',
            context={
                'user': 'Maciej'
            }
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
            deadline = Reservation(date_of_reservation=date_post, end_time=time_post, order_dish_id=1,
                                   table_id=table_post, client_id=1, start_time=time_post)
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
                'table_post': table_post
            }
        )



class MenuView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request,
                      template_name='Menu.html',
                      context={'categories': categories})

class CategoryView(View):
    def get(self, request, id):
        selected_category = Category.objects.get(pk=id)
        dish_received = Dish.objects.filter(category=selected_category)
        categories = Category.objects.all()
        return render(request,
                      template_name='Category.html',
                      context={'selected_category': selected_category,
                               'dish_received': dish_received,
                               'categories': categories})


class DishView(View):
    def get(self, request, id):
        dishes = Dish.objects.get(pk=id)
        categories = Category.objects.all()
        return render(request,
                      template_name="Dishes.html",
                      context={'dishes': dishes,
                               'categories': categories})

# def order_view(request, id):
#     order = OrderDish.objects.get(pk=id)
#     dishes = Dish.objects.filter(order_view=order)
#     dane = {'order': order,
#             'dishes': dishes}
#     return render(request, 'Ordered.html', dane)
class OrderView(View):
    ordered = []

    def post(self, request):
        order = request.POST.get('dish_id', None)
        return render(request,
                      template_name='Ordered.html',
                      context={'order': order})
                      context={'order': order,
                               })
    # def get(self, request):
    #     categories = Category.objects.all()
    #     return render(request,
    #                   template_name='Ordered.html',
    #                   context={
    #                            'categories': categories
    #                            })





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
