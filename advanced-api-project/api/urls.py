from django.urls import path
from .views import (
    BookCreateView, 
    BookDeleteView, 
    BookDetailView, 
    BookListView, 
    BookUpdateView
)

urlpatterns = [
    path("books/create", BookCreateView.as_view(), name="create-book"),
    path("books/delete/<int:pk>/", BookDeleteView.as_view(), name="delete-book"),
    path("books/details", BookDetailView.as_view(), name="book-details"),
    path("books/list", BookListView.as_view(), name="list-books"),
    path("books/update/<int:pk>/", BookUpdateView.as_view(), name="update-book"),
]