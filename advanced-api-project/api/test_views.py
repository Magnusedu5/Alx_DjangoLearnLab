from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author
from django.urls import reverse

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user and authenticate
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")

        # Create sample author and book
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(title="Book 1", publication_year=2020, author=self.author)

    def test_update_book(self):
        url = reverse("update-book", args=[self.book.id])
        data = {"title": "Updated Title", "publication_year": 2021, "author": self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse("delete-book", args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
