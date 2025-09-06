from django.urls import path
from .views import list_books, LibraryDetailView, home_redirect


urlpatterns = [
    path('', home_redirect, name='home_redirect'),  # 👈 Handles root URL

    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]