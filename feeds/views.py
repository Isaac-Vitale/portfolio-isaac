from django.shortcuts import render
from .models import *

# Create your views here.


def home_page(request):
    myinfo = PersonalInformation.objects.all()
    context = {
        "info": myinfo,
    }

    return render(request, 'home_page.html', context)
