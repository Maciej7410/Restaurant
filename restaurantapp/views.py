from django.shortcuts import render
from django.views import View
from restaurantapp.models import Client


# Create your views here.

class ClientV(View):
    def get(self, request):
        return render(
            request,
            template_name='Hello.html',
            context={'Client': Client.objects.all()}
        )
