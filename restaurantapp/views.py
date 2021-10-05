from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, ListView

from restaurantapp.models import Table, Reservation, Category
import time
from restaurantapp.forms import ReservationForm, DishForm, CategoryForm


# Create your views here.
# class ReservationFormView(FormView):
#     template_name = 'TestForms.html'
#     from_class = ReservationForm
# model = Reservation
# extra_context = {
#     'reservation': Reservation.objects.all()
# }
class ReservationFormView(FormView):
    template_name = 'TestForms.html'
    Form_class = ReservationForm
    model = Reservation


class DishFormView(FormView):
    template_name = 'TestForms.html'
    Form_class = DishForm


class CategoryFormView(FormView):
    template_name = 'TestForms.html'
    Form_class = CategoryForm


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
