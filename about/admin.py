from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Aboutus, AboutInfo


@admin.register(Aboutus)
class AboutusAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']

@admin.register(AboutInfo)
class AboutinfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'description']





    