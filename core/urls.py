# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('buy-now/<int:service_id>/', views.buy_now, name='buy_now'),
    path('invoice/<int:invoice_id>/', views.Invoice, name='invoice'),
    ]
