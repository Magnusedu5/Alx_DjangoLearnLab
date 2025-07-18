from django.shortcuts import render
from .models import Book
from django.views.generic import ListView

# Create your views here.
def list_books(request):
    Book.objects.all()
    return render (request, 'relationship_app/list_books.html')


class bookviews(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'