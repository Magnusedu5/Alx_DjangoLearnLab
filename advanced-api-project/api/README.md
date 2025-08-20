Django Book CRUD Project

A simple Django application demonstrating CRUD operations (Create, Read, Update, Delete) for a Book model using class-based generic views (django.views.generics).

This project also showcases read-only permissions for unauthenticated users and restricted write permissions for authenticated users.

🚀 Features

List all books (publicly accessible).

View book details (publicly accessible).

Create new book (authenticated users only).

Update existing book (authenticated users only).

Delete a book (authenticated users only).

Permissions:

Unauthenticated users → can only read (List & Detail).

Authenticated users → can create, update, delete.