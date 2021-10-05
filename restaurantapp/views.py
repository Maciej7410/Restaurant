from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from restaurantapp.forms import LoginForm
from django.views.generic import CreateView
from restaurantapp.forms import RegisterView
from django.urls import reverse_lazy
from restaurantapp.models import Table, Category, Dish, Reservation

import time






# @csrf_exempt
class MenuRegistration(View):
    def get(self, request):
        return render(
            request,
            template_name='Registration.html',
            context={
                'user': 'Maciej'
            }
        )

    def post(self, request):
        result = ""
        set = ''
        date_post = request.POST.get('date', 'none')
        date_post = time.strptime(str(date_post), "%Y-%m-%d")
        time_post = request.POST.get('time', 'none')
        table_post = request.POST.get('table', 'none')

        registration_db = Reservation.objects.all()
        for start_date in registration_db:

            if time.strptime(str(start_date.date_of_reservation), "%Y-%m-%d") == date_post:
                result = "Zajęte"
                set = start_date.date_of_reservation
            else:
                set = start_date.date_of_reservation
                # deadline = Reservation(date_of_reservation=date_post, start_time=time_post, table_id=1)
                # deadline.save()
                table = Table(name=date_post, description=time_post, sits='2')
                table.save()
                result = "Zapisano termin"




def menu_view(request):
    categories = Category.objects.all()
    dane = {'categories': categories}
    return render(request, 'Menu.html', dane)


def category_view(request, id):
    category_user = Category.objects.get(pk=id)
    dish_category = Dish.objects.filter(category=category_user)
    categories = Category.objects.all()
    dane = {'category_user': category_user,
            'dish_category': dish_category,
            'categories': categories}
    return render(request, 'Category.html', dane)


def dish_view(request, id):
    dishes = Dish.objects.get(pk=id)
    categories = Category.objects.all()
    dane = {'dishes': dishes, 'categories': categories}
    return render(request, 'Dishes.html', dane)

# def order_view(request, id):
#     order = OrderDish.objects.get(pk=id)
#     dishes = Dish.objects.filter(order_view=order)
#     dane = {'order': order,
#             'dishes': dishes}
#     return render(request, 'Ordered.html', dane)
class OrderView(View):
    def post(self, request):
        order = request.POST.get('dish_id', 'None')
        return render(request, template_name='Ordered.html', context={'dish_name': Dish.objects.filter(id=order)})



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



class RegisterUser(CreateView):
    template_name = 'Register.html'
    form_class = RegisterView
    success_url = reverse_lazy('main')

class LogOutUser(LogoutView):
    template_name = 'Logout.html'
    def log_out(self,request):
        logout(request)