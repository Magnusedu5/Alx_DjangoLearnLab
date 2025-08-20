from django.shortcuts import render
from django.views import generic
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BookListView(generic.ListView):
    model = Book
    template_name = "api/templates/list_books.html"
    ordering = ["title"]
    context_object_name = "books"

class BookDetailView(generic.DetailView):
    model = Book
    template_name = "api/templates/details_books.html"
    context_object_name = "book"


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    template_name = "api/templates/create_books.html"
    fields = ["title", "author", "published_date"]
    login_url = "/login/"  # Redirect if not logged in

    def form_valid(self, form):
        title = form.cleaned_data["title"]
        author = form.cleaned_data["author"]

        # Validation: same title + author should not exist
        if Book.objects.filter(title=title, author=author).exists():
            form.add_error(None, "A book with this title and author already exists.")
            return self.form_invalid(form)

        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    template_name = "api/templates/update_books.html"
    fields = ["title", "author", "published_date"]
    login_url = "/login/"  # Redirect if not logged in
    
    def form_valid(self, form):
        title = form.cleaned_data["title"]
        author = form.cleaned_data["author"]

        # Exclude current book from duplicate check
        if Book.objects.filter(title=title, author=author).exclude(pk=self.object.pk).exists():
            form.add_error(None, "Another book with this title/author already exists.")
            return self.form_invalid(form)

        return super().form_valid(form)

class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    template_name = "api/templates/delete_books.html"
    login_url = "/login/"  # Redirect if not logged in
    