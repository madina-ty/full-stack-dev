class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} — {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        return results

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        for i, book in enumerate(available_books, start=1):
            print(f"{i}. {book}")

    def borrow_book(self, title, user):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                user.borrowed_books.append(book)
                print(f"Книга \"{title}\" успешно выдана {user.name}.")
                return
        print("Книги с таким названием нет или она уже выдана.")

    def return_book(self, title, user):
        for book in user.borrowed_books:
            if book.title == title:
                book.is_available = True
                user.borrowed_books.remove(book)
                print(f"Книга \"{title}\" возвращена.")
                return
        print("У вас нет такой книги.")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrowed_books(self):
        print(f"Книги, взятые {self.name}:")
        for book in self.borrowed_books:
            print(f"- {book}")


library = Library()
library.add_book(Book("1984", "Джордж Оруэлл", "12345"))


while True:
    user_name = input("Введите имя пользователя (или 'стоп' для выхода): ")
    if user_name == 'стоп':
        break
    user = User(user_name, 123)  # Замените 123 на реальный ID пользователя
    library.list_available_books()
    book_title = input("Введите название книги, которую хотите взять: ")
    library.borrow_book(book_title, user)
    user.borrowed_books()