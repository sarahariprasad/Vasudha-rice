from django.shortcuts import render
from .models import Certificates, CertificatesImages, CertificatesTitle

# Create your views here.
def certs_all(request):
    template_name = 'about/certificates.html'
    certs = Certificates.objects.all()
    certsimg = CertificatesImages.objects.all()
    certstitle = CertificatesTitle.objects.all()
    context = {
        "certs" : certs,
        "certsimg" : certsimg,
        "certstitle" : certstitle
    }
    return render (request, template_name, context)