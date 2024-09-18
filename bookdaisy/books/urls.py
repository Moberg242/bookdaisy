from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('about/', views.about, name='about'),
    path('bookshelf/', views.home, name='home'),
    path('bookshelf/edit', views.EditShelf.as_view(), name='edit_bookshelf'),
    path('addbook/', views.AddBook.as_view(), name='add_book'),
    path('library/<sorted>/', views.Index.as_view(), name='index'),
    path('library/<sorted>/tbr/', views.Tbr.as_view(), name='tbr'),
    path('search/', views.SearchTitle.as_view(), name='search_title'),
    path('book/<int:pk>/', views.BookDetails.as_view(), name='book_details'),
    path('book/<int:pk>/delete', views.DeleteBook.as_view(), name='delete_book'),
    path('book/<int:pk>/update', views.UpdateBook.as_view(), name='update_book'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/theme/', views.change_theme, name='change_theme'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Used this helpful youtube video as well as django docs to figure out images! https://youtu.be/GNsuF4xB80E?si=MYDA7E6ZrRfeikjK
