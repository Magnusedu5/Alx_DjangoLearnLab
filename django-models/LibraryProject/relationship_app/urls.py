# relationship_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('view_books/', views.bookviews, name='list_books')
]
