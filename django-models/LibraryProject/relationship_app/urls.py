from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('view_books/<int:pk>/', views.LibraryDetailView.as_view(), name='view_books')
]
