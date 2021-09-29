from django.shortcuts import render
from django.views import View
from restaurantapp.models import Table, Category


# Create your views here.

class ClientV(View):
    def get(request):
        return render(
            request,
            template_name='Hello.html',
            context={'clients': Table.objects.all()}
        )

def MenuView(request):
    Categories = Category.objects.all()
    dane = {'Categories' : Categories}
    return render(request, 'Menu.html', dane)
