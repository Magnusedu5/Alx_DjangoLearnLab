from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView

# Create your views here.
def list_books(request):
    Book.objects.all()
    return render (request, 'relationship_app/list_books.html')


class Bookviews(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'