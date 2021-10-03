from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from restaurantapp.models import Table, Reservation
import time
from restaurantapp.forms import DishForm
from django.views.generic import ListView

# Create your views here.
class DishesView(FormView):
    template_name = 'TestForms.html'
    # from_class = DishForm
    model = Reservation

class RegistrationViews(ListView):
    template_name = 'TestForms.html'
    from_class = DishForm
    model = Reservation

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

        return render(
            request,
            template_name='Registration.html',
            context={
                'user': 'Maciej',
                'date': date_post,
                'time': time_post,
                'table': table_post,
                'result': result,
                'start_date': "start_date.date_of_reservation",
                'set': set
            }
        )
