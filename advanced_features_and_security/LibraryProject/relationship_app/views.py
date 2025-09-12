from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, TemplateView
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login

from .models import Author, Book, Library, UserProfile
from .forms import BookForm

# ─── Book Views ──────────────────────────────────────────────
@login_required(login_url='login')
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

@permission_required('relationship_app.can_add_book')
def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list-books')
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list-books')
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list-books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# ─── Library Detail ──────────────────────────────────────────
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.get_object().books.all()
        return context

# ─── Role-Based Views ────────────────────────────────────────
def has_role(user, role):
    return UserProfile.objects.filter(user=user, role=role).exists()

@user_passes_test(lambda u: has_role(u, "Admin"))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: has_role(u, "Librarian"))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: has_role(u, "Member"))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# ─── Auth & Profile ──────────────────────────────────────────
class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class ProfileView(TemplateView):
    template_name = 'relationship_app/profile.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

class LoginPage(LoginView):
    template_name = 'relationship_app/login.html'

class LogoutPage(LogoutView):
    template_name = 'relationship_app/logout.html'

# ─── Home Redirect ───────────────────────────────────────────
@login_required(login_url='login')
def home_redirect(request):
    return redirect('list-books')