from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import LoginPage, LogoutPage, RegisterView
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('login/', LoginPage.as_view(template_name='relationship_app/login.html'), name='login'),
    
    path('logout/', LogoutPage.as_view(template_name='relationship_app/logout.html'), name='logout'),
 
    path('register/', RegisterView.as_view(), name='register'),

    path('register/', views.register, name='register'), 

    path('admin/', views.admin_view, name='admin_view'),

    path('librarian/', views.librarian_view, name='librarian_view'),

    path('member/', views.member_view, name='member_view'),

    path("add/", views.add_book, name="add_book"),

    path("edit/<int:book_id>/", views.edit_book, name="edit_book"),

     path("delete/<int:book_id>/", views.delete_book, name="delete_book"),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('booklist/',views.booklist, name = "booklist"),
    
    path('', views.home_redirect, name='home'),
     
]  