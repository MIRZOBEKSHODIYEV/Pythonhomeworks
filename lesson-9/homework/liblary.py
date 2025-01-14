class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"


class Member:
    MAX_BORROWED_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BORROWED_BOOKS:
            print(f"{self.name} cannot borrow more than {self.MAX_BORROWED_BOOKS} books.")
            return
        if book.is_borrowed:
            print(f"The book '{book.title}' is already borrowed.")
            return
        self.borrowed_books.append(book)
        book.is_borrowed = True
        print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def __str__(self):
        books = ', '.join(book.title for book in self.borrowed_books) or "No books"
        return f"Member: {self.name}, Borrowed books: {books}"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author):
        if title in self.books:
            print(f"The book '{title}' is already in the library.")
        else:
            self.books[title] = Book(title, author)
            print(f"Added '{title}' by {author} to the library.")

    def add_member(self, name):
        if name in self.members:
            print(f"Member '{name}' already exists.")
        else:
            self.members[name] = Member(name)
            print(f"Added member '{name}'.")

    def borrow_book(self, member_name, book_title):
        if member_name not in self.members:
            print(f"Member '{member_name}' not found.")
            return
        if book_title not in self.books:
            print(f"The book '{book_title}' does not exist in the library.")
            return

        member = self.members[member_name]
        book = self.books[book_title]
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        if member_name not in self.members:
            print(f"Member '{member_name}' not found.")
            return
        if book_title not in self.books:
            print(f"The book '{book_title}' does not exist in the library.")
            return

        member = self.members[member_name]
        book = self.books[book_title]
        member.return_book(book)

    def __str__(self):
        books = "\n".join([str(book) for book in self.books.values() if not book.is_borrowed]) or "No available books"
        members = "\n".join([str(member) for member in self.members.values()]) or "No members"
        return f"Library Books:\n{books}\n\nMembers:\n{members}"


# Simple Test
if __name__ == "__main__":
    library = Library()

    library.add_book("O'tgan kunlar ", "Abdulla Qodiriy")
    library.add_book("Besh bolali yigitcha", "Xudoyberdi To'xtaboyev")

    library.add_member("Mirzobek")
    library.add_member("Lazizbek")
    library.add_member("Shaxzod")

    library.borrow_book("Mirzobek", "O'tgan kunlar")
    library.borrow_book("Lazizbek", "Besh bolali yigitcha")
    library.borrow_book("Shaxzod", "O'tgan kunlar")  # Already borrowed

    library.return_book("Mirzobek", "O'tgan kunlar")
    library.return_book("Mirzobek", "Besh bolali yigitcha")

    print("\nLibrary State:")
    print(library)
