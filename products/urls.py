from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='products'),
    path('category/<int:pkid>', views.show_category, name='show_category'),

]
