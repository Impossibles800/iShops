from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('reset_password', views.reset_password, name='reset_password'),
]
