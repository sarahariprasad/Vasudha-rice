from django.shortcuts import render
from .models import Gallery, Gallerytwo, GalleryTitle

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def gallery_all(request):
    template_name = 'about/gallery.html'
    gallery = Gallery.objects.all()
    gallerytwo = Gallerytwo.objects.all()
    gallerytitle = GalleryTitle.objects.all()
    context = {
        "gallery" : gallery,
        "gallerytwo" : gallerytwo,
        "gallerytitle" : gallerytitle
    }
    return render (request, template_name, context)
