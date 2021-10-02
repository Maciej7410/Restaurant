from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from restaurantapp.models import Table


# Create your views here.

class ClientV(View):
    def get(request):
        return render(
            request,
            template_name='Hello.html',
            context={'clients': Table.objects.all()}
        )

class MenuView(View):
    def get(request):
        return render(
            request,
            template_name='Menu.html',
            context={'menu': 'Menu'}
        )
@csrf_exempt
class MenuRegistration(View):
    def post(request):
        return render(
            request,
            template_name='Registration.html',
            context={
                'user': 'Maciej'
            }

        )