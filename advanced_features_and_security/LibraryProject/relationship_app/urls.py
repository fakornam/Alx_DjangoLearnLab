from django.urls import path
from . import views

urlpatterns = [
    # ─── Book Management ─────────────────────────────────────
    path('books/', views.list_books, name='list-books'),
    path('add_book/', views.add_book, name='add-book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit-book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete-book'),

    # ─── Library ─────────────────────────────────────────────
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    # ─── Role-Based Access ───────────────────────────────────
    path('admin/', views.admin_view, name='admin-view'),
    path('librarian/', views.librarian_view, name='librarian-view'),
    path('member/', views.member_view, name='member-view'),

    # ─── Auth & Profile ──────────────────────────────────────
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.LogoutPage.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    # ─── Home ────────────────────────────────────────────────
    path('', views.home_redirect, name='home'),
]