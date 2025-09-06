# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library 


# Function-Based View: List Books

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Library Detail

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    
# Optional redirect view for root URL
def home_redirect(request):
    return redirect('list_books')
