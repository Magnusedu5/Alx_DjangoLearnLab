from relationship_app.models import Author, Book, Library, Librarian

author_name = "Chinua Achebe"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

library_name = "State Library"
library = Library.objects.get(name=library_name) 
books_in_library = library.books.all()

librarian = Librarian.objects.get(Library=library_name)