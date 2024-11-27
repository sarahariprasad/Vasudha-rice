from django.db import models
from datetime import datetime

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    submitted_on = models.DateTimeField(default=datetime.now)
    message = models.TextField()


    def __str__(self):
        return self.name
