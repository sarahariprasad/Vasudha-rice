from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import AuthenticationForm
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model



from .forms import RegistrationForm
from .models import UserBase
from .tokens import account_activation_token
from django.core.mail import send_mail



@login_required
def dashboard(request):
    return render(request, 'account/user/dashboard.html')

def account_register(request):

     
     
     if request.method == 'POST':
         registerForm = RegistrationForm(request.POST)
         if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            login(request, user)
            return redirect("account:dashboard")
           
           
         
         else:
             return render(request, 'account/registration/activation_invalid.html')

            
     else:
       registerForm = RegistrationForm()
       return render(request, 'account/registration/register.html', {'form': registerForm})
     





    