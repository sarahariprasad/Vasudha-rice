from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    #path('', views.BasketView, name='basket'),
    path('create-order/', views.create_order, name='create_order'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),
    path('order-history/', views.order_history, name='order_history'),
    path('order/cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),

]