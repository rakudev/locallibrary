from django.shortcuts import render

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
    
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_genres_with_fiction = Genre.objects.filter(name__icontains='fiction').count()
    num_books_with_I = Book.objects.filter(title__icontains='I').count()
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_with_fiction' : num_genres_with_fiction,
        'num_books_with_I': num_books_with_I,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)
