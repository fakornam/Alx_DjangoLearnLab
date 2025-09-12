from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import News, news_id
from .models import Book
from .forms import BookSearchForm
from .forms import ExampleForm

def example_view(request):
    form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form" : form})


def book_list(request):
    form = BookSearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data["query"]
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, "bookshelf/book_list.html", {"form" : form, "books" : books})

# creating the books list 

def book_list(request):
    query = request.GET.get("search", "")
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
        return render(request, "bookshelf/book_list.html", {"books" : books})
    

# View to list the News (or books)
@permission_required("bookshelf.can_view_news", raise_exception=True)
def book_list(request):
    # Query to get all the news from the database
    news = News.objects.all()
    return render(request, "book_list.html", {"news": news})

@permission_required("bookshelf.can_create_news", raise_exception=True)
def create_news(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        News.objects.create(title=title, content=content)
        return render(request, "bookshelf/news.html")
    return render(request, "bookshelf/create_news.html")

# Edit the News (require can_edit_news permission)
@permission_required("bookshelf.can_edit_news", raise_exception=True)
def edit_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    if request.method == "POST":
        title = request.POST["title"]
        news.title = request.POST["title"]
        news.content = request.POST["content"]
        news.save()
        return render(request, "bookshelf/news.html")
    return render(request, "bookshelf/edit_news.html", {"news": news})

# View the News (required can_view_news permission)
@permission_required("bookshelf.can_view_news", raise_exception=True)
def view_news(request):
    news = get_object_or_404(News, pk=news_id)
    return render(request, "bookshelf/view_news.html", {"news": news})

# Delete the News (required can_delete_news permission)
@permission_required("bookshelf.can_delete_news", raise_exception=True)
def delete_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    news.delete()
    return render(request, "bookshelf/news_deleted.html")

# Create your views here.

def homepage(request):
    template = "bookshelf/home.html/"
    return render(request, template_name=template, context={})