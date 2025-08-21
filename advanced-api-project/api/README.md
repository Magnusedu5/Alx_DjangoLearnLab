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

Filtering, Searching, and Ordering

This API supports filtering, searching, and ordering to give users flexibility when retrieving books.

1. Filtering

You can filter books by specific fields.
Example:

GET /books/?publication_year=2020

2. Searching

Search across title and author fields with partial matches.
Example:

GET /books/?search=tolkien


This will return all books with "tolkien" in the title or author field.

3. Ordering

Order the results by one or more fields such as title or publication_year.

Examples:

# Order by title ascending
GET /books/?ordering=title

# Order by title descending
GET /books/?ordering=-title

# Order by publication year descending
GET /books/?ordering=-publication_year

# Order by multiple fields
GET /books/?ordering=publication_year,title

⚙️ Default Ordering

If no ordering is specified, results are ordered by title by default.