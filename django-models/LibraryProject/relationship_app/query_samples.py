from relationship_app.models import Author, Book, Library

Author.objects.create(name="Magnus Edu")

author_name = "Magnus Edu"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")

Library.objects.create(name="State Library")
library_name = "State Library"
library = Library.objects.get(name=library_name)
books_in_library = Book.objects.all()
print(f"\nBooks in {library_name}:")
for book in books_in_library:
    print(f " - {book.title}")

librarian = library.librarian
print(f"\nLibrarian for {library_name}: {librarian.name}")
