from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addbook/', views.add_book, name='add_book'),
    path('library/', views.Index.as_view(), name='index'),
    path('book/<int:pk>/delete', views.DeleteBook.as_view(), name='delete_book'),
    path('book/<int:pk>/update', views.UpdateBook.as_view(), name='update_book'),
]