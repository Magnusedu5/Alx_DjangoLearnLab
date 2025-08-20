from django.urls import path
from .views import (
    BookCreateView, 
    BookDeleteView, 
    BookDetailView, 
    BookListView, 
    BookUpdateView
)

urlpatterns = [
    path("books/add", BookCreateView.as_view(), name="create-book"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="delete-book"),
    path("books/<int:pk>", BookDetailView.as_view(), name="book-details"),
    path("books/list", BookListView.as_view(), name="list-books"),
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="update-book"),
]