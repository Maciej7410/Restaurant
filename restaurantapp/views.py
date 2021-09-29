from django.shortcuts import render, HttpResponse
from django.views import View
from restaurantapp.models import Table, Category, Dish


# Create your views here.

class ClientV(View):
    def get(request):
        return render(
            request,
            template_name='Hello.html',
            context={'clients': Table.objects.all()}
        )


def CategoryView(request):
    Categories = Category.objects.all()
    dane = {'Categories': Categories}
    return render(request, 'Menu.html', dane)




def DishView(request, id):
    dishes = Dish.objects.get(pk=id)
    Categories = Category.objects.all()
    dane = {'dishes': dishes, 'categories': Categories}
    return render(request, 'Dishes.html', dane)
