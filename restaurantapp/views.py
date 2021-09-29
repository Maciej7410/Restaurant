from django.shortcuts import render
from django.views import View
from restaurantapp.models import Client



class ClientV(View):
    def get(request):
        return render(
            request,
            template_name='Hello.html',
            context={'client': Client.objects.all()}
        )
class MenuView(View):
    def get(request):
        return render(
            request,
            template_name='Menu.html',
            context={'menu': 'Menu'}
        )
