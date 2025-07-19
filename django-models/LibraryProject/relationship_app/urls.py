from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import (
    list_books,
    LibraryDetailView,
    register,
    admin_view,
    librarian_view,
    member_view,
    CustomLoginView  # use this instead of LoginView
)

urlpatterns = [
    # Book-related views
    path('list_books/', list_books, name='list_books'),
    path('view_books/<int:pk>/', LibraryDetailView.as_view(), name='view_books'),

     # Add book
    path('add_book/', views.add_book, name='add_book'),

    # Edit book
    path('edit_book/<int:book_id>/', views.update_book, name='edit_book'),

    # Delete book
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    # Authentication views
    path('login/', CustomLoginView.as_view(), name='login'),  # 👈 use your custom login
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),

    # Role-based views
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
