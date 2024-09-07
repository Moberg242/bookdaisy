from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('addbook/', views.add_book, name='add_book'),
    path('library/', views.Index.as_view(), name='index'),
    path('search/', views.SearchTitle.as_view(), name='search_title'),
    path('book/<int:pk>/', views.BookDetails.as_view(), name='book_details'),
    path('book/<int:pk>/delete', views.DeleteBook.as_view(), name='delete_book'),
    path('book/<int:pk>/update', views.UpdateBook.as_view(), name='update_book'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Used this helpful youtube video as well as django docs to figure out images! https://youtu.be/GNsuF4xB80E?si=MYDA7E6ZrRfeikjK
