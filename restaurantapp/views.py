from django.shortcuts import render
from django.views import View
from restaurantapp.models import Client


# Create your views here.

class ClientV(View):
    def get(request):
        return render(
            request,
            template_name='Hello.html',
            context={'client': Client.objects.all()}
        )
