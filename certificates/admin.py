from django.contrib import admin
from .models import Certificates, CertificatesImages, CertificatesTitle

# Register your models here.

@admin.register(Certificates)
class Certificate(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']

@admin.register(CertificatesImages)
class CertificateImages(admin.ModelAdmin):
    list_display = ['image']

@admin.register(CertificatesTitle)
class CertificateTitle(admin.ModelAdmin):
    list_display = ['title']