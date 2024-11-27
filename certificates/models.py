from django.db import models

# Create your models here.
class Certificates(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description

class CertificatesImages(models.Model):
    image = models.ImageField(upload_to='images/', null=True )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description
    
class CertificatesTitle(models.Model):
    title = models.TextField(blank=True)

    def __str__(self):
        return self.title