from django.shortcuts import render
from django.views import View
from restaurantapp.models import Table, Category, Dish, OrderDish


# Create your views here.

class ClientV(View):
    def get(request):
        return render(
            request,
            template_name='Hello.html',
            context={'clients': Table.objects.all()}
        )


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
