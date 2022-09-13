from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='products'),
    path('category/<int:pkid>', views.show_category, name='show_category'),
    path('search/', views.search, name='search'),
    path('buy/<int:pkid>', views.buy, name='buy'),
]
