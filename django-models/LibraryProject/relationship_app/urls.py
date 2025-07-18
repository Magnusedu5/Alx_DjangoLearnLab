from django.urls import path
from . import views
from .views import list_books, Bookviews

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('view_books/', views.Bookviews, name='view_books')
]
