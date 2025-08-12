class book:
    def __init__(self, name, is_issued=False):
        self.name = name
        self.is_issued = is_issued


class library:
    def __init__(self):
        self.books = []

    def save_to_file(self):
        with open("Library_books.txt", "w") as file:
            for book in self.books:
                status = "Issued to someone" if book.is_issued else "Available"
                file.write(f"Book : {book.name} | Status : {status}\n")

    def add_book(self, b):
        self.books.append(b)
        self.save_to_file()

    def issue_book(self, title):
        for book in self.books:
            if book.name == title and book.is_issued == False:
                book.is_issued = True
                self.save_to_file()
                print("Book Issued Successfully.")
                return
        print("Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book.name == title and book.is_issued:
                book.is_issued = False
                self.save_to_file()
                print("Book Returned Successfully.")
                return
        print("Book not found or not issued.")

    def show_books(self):
        for book in self.books:
            print(
                f"Book : {book.name} | Status : {"Issued" if book.is_issued else "Avilable"}"
            )


lib = library()
b1 = book("Beyond Truth")
b2 = book("We")
b3 = book("Hope So")
b4 = book("Matrix")
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_book(b4)
lib.show_books()
lib.issue_book("We")
lib.issue_book("Hope So")
lib.show_books()
lib.return_book("We")
lib.show_books()
