from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated] 


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 