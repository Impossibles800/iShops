from django.urls import path
from payment import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('checkout/', views.checkout, name='checkout'),
    ]
