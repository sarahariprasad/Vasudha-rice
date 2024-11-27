from django.urls import path

from . import views

app_name = 'certificates'

urlpatterns = [
   path('', views.certs_all, name='certs_all'),
    
]