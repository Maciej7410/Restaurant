from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from restaurantapp.forms import LoginForm
from django.views.generic import CreateView
from restaurantapp.forms import RegisterView
from django.urls import reverse_lazy
from restaurantapp.models import Table, Category, Dish, Reservation, OrderDish, OrderList
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


class OrderView(View):
    ordered = []
    def post(self, request):
        order = request.POST.get('dish_id', None)
        return render(request,
                      template_name='Ordered.html',
                      context={'order': order,
                               'ordered': ordered})
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
