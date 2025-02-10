class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, copies=1):
        self.books[title] = self.books.get(title, 0) + copies

    def borrow_book(self, title):
        if self.books.get(title, 0) > 0:
            self.books[title] -= 1
            print(f"Borrowed: {title}")
        else:
            print(f"{title} is not available.")

    def return_book(self, title):
        self.books[title] = self.books.get(title, 0) + 1
        print(f"Returned: {title}")

    def available_books(self):
        return {title: copies for title, copies in self.books.items() if copies > 0}

# Example Usage
if __name__ == "__main__":
    library = Library()
    library.add_book("math analysis", 2)
    library.borrow_book("math analysis")
    library.return_book("math analysis")
    print("Available books:", library.available_books())
