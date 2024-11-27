from django.db import models

# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Gallerytwo(models.Model):
    image = models.ImageField(upload_to='images/', null=True )
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.description
    
class GalleryTitle(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title
