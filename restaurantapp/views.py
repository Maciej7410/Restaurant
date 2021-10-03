from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from restaurantapp.forms import LoginForm
from django.views.generic import CreateView
from restaurantapp.forms import RegisterView
from django.urls import reverse_lazy


# Create your views here.


class MenuView(View):
    def get(self, request):
        return render(
            request,
            template_name='Menu.html',
            context={'menu': 'Menu'}
        )


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
