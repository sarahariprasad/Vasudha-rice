from django.contrib import admin

from .models import Gallery, Gallerytwo, GalleryTitle


@admin.register(Gallery)
class Gallery(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']

@admin.register(Gallerytwo)
class Gallerytwo(admin.ModelAdmin):
    list_display = ['image', 'description']

@admin.register(GalleryTitle)
class GalleryTitle(admin.ModelAdmin):
    list_display = ['title']