from django.shortcuts import render

# Create your views here.
# relationship_app/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from .models import Book
from .forms import BookForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book-list')
    return render(request, 'books/edit.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    Book.objects.get(pk=book_id).delete()
    return redirect('book-list')

from .models import Book
from django.shortcuts import render

def search_books(request):
    query = request.GET.get('q', '')
    results = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/list_books.html', {'books': results})
