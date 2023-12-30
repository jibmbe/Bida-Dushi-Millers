# core/urls.py
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import PortfolioView

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('buy-now/<int:service_id>/', views.buy_now, name='buy_now'),
    path('invoice/<int:invoice_id>/', views.Invoice, name='invoice'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    ]
