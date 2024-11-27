from django.shortcuts import render
from .models import Aboutus, AboutInfo

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def about_all(request):
    template_name = 'about/about.html'
    aboutlist = Aboutus.objects.all()
    aboutinfo = AboutInfo.objects.all()
    context = {
        "aboutlist" : aboutlist,
        "aboutinfo" : aboutinfo
    }
    return render (request, template_name, context)






    