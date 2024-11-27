from django.db import models



# Create your models here.

class Aboutus(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class AboutInfo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True )
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    






