from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addbook/', views.add_book, name='add_book'),
]