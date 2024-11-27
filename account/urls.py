from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import ( UserLoginForm, PwdResetConfirmForm,PwdResetForm)
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetCompleteView
#from django.urls import include, path


app_name = 'account'

urlpatterns = [
    
   
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    
    path('register/', views.account_register, name='register'),
    
   
   ##### Password Reset URL's #######
   path('password_reset/', auth_views.PasswordResetView.as_view(template_name="forgotpassword/password_reset_form.html",
                                                                 success_url='password_reset_email_confirm',
                                                                 email_template_name='forgotpassword/password_reset_email.html',
                                                                 form_class=PwdResetForm), name='pwdreset'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='forgotpassword/password_reset_confirm.html',
                                                                                                success_url='/account/password_reset_complete/', 
                                                                                                form_class=PwdResetConfirmForm),
         name="password_reset_confirm"),
    path('password_reset/password_reset_email_confirm/',
         TemplateView.as_view(template_name="forgotpassword/password_reset_sent.html"), name='password_reset_done'),
    path('password_reset_complete/',
         TemplateView.as_view(template_name="forgotpassword/password_reset_complete.html"), name='password_reset_complete'),
   
   # User dashboard
    path('dashboard/', views.dashboard, name='dashboard'),


]