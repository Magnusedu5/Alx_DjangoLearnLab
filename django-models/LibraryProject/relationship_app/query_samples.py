from relationship_app.models import Author, Book

author = Author.objects.get(name="Chinua Achebe")
books = Book.objects.filter(author=author)

library_name = "State Library"
library = Library.objects.get(name=library_name) 
books_in_library = library.books.all()

library = Library.objects.get(name="State Library")
librarian = library.librarian