from abc import ABC, abstractmethod
import json
import os


class LibraryActions(ABC):
    @abstractmethod
    def search_books(self, book, library):
        pass

    @abstractmethod
    def view_books(self, library):
        pass


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._is_availible = True

    def check_book_availability(self):
        return self._is_availible

    def set_book_availability(self, status):
        self._is_availible = status

    def show_book_details(self):
        print(
            f"Title : {self.title}, Author : {self.author}, ISBN : {self.isbn}, Availability : {self.check_book_availability()}"
        )


class User:
    def __init__(self, name, email, userid, password):
        self.name = name
        self.email = email
        self.userid = userid
        self.__password = password

    def set_password(self, old_pwd, new_pwd):
        if self.__password == old_pwd:
            self.__password = new_pwd
            print("Password Updated Successfully!")
        else:
            print("Incorrect old password!")

    def get_password(self):
        return self.__password

    def login(self, pwd, id):
        if pwd == self.__password and id == self.userid:
            print(f"{self.name} logged in.")
            return True

    def logout(self):
        print(f"{self.name} logged out.")

    def write_book_data(self, library):
        books_list = []
        for book in library:
            books_list.append(
                [book.title, book.author, book.isbn, book.check_book_availability()]
            )
        with open("books_data.json", "w") as file:
            json.dump(books_list, file, indent=4)

    def get_book_data(self):
        lib = []
        if not os.path.exists("books_data.json"):
            return lib
        with open("books_data.json", "r") as file:
            books_list = json.load(file)
        for title, author, isbn, availability in books_list:
            b = Book(title, author, isbn)
            b.set_book_availability(availability)
            lib.append(b)
        return lib


class Admin(User):

    def add_book(self, library, book):
        library.append(book)
        print("Book added successfully!")

    def remove_book(self, library, book_id):
        for b in library:
            if b.isbn == book_id:
                library.remove(b)
                print("Book removed from library.")
                break
        else:
            print("Book is not in library.")

    def view_reports(self, library):
        print(f"Number of books available : {len(library)}\n")

        for i, book in enumerate(library):
            status = "Available" if book.check_book_availability() else "Unavailable"
            print(
                f"{i+1}. {book.title} written by {book.author}, ISBN : {book.isbn}, Status : {status}"
            )

    def all_members_Details(self, members, library):

        for i, member in enumerate(members):
            member.load_borrowed_books(library)
            print(
                f"\n{i+1}. Name : {member.name}, Email : {member.email}. Id : {member.userid}\n"
            )
            print("Borrowed Books : ")
            r = 0
            for bb in member.borrowed_books:
                print(f"{r+1}. {bb.title} written by {bb.author}, ISBN : {bb.isbn}")
                r += 1


class Librarian(User, LibraryActions):
    def view_books(self, library):
        for i, book in enumerate(library):
            print(
                f"{i+1}. Title : {book.title}, Author : {book.author}, ISBN : {book.isbn}, Availability : {book.check_book_availability()}"
            )

    def search_books(self, book_id, library):
        for book in library:
            if book.isbn == book_id:
                status = (
                    "Available" if book.check_book_availability() else "Unavailable"
                )
                print(
                    f"Title : {book.title}, Author : {book.author}, ISBN : {book.isbn}, Availability : {status}"
                )
                break
        else:
            print("Book not found.")

    def issue_book(self, book_id, library, member):
        for b in library:
            if b.isbn == book_id:
                if b.check_book_availability():
                    b.set_book_availability(False)
                    member.borrowed_books.append(b)
                    print("Book Issued successfully!")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book_id, library, member):

        for book in member.borrowed_books:
            if book.isbn == book_id:
                book.set_book_availability(True)
                member.borrowed_books.remove(book)
                print("Book Returned Successfully.")
                return

        for book in library:
            if book.isbn == book_id:
                print("This member has not borrowed that book.")
                return

        print("Book not found in library.")


class Member(User, LibraryActions):

    def __init__(self, name, email, userid, password):
        super().__init__(name, email, userid, password)
        self.borrowed_books = []

    def view_books(self, library):
        for i, book in enumerate(library):
            print(
                f"{i+1}. Title : {book.title}, Author : {book.author}, ISBN : {book.isbn}, Availability : {book.check_book_availability()}"
            )

    def search_books(self, book_id, library):
        for book in library:
            if book.isbn == book_id:
                print(
                    f"Title : {book.title}, Author : {book.author}, ISBN : {book.isbn}, Availability : {book.check_book_availability()}"
                )
                break
        else:
            print("Book not found.")

    def borrow_book(self, book_id, library):
        for book in library:
            if book.isbn == book_id and book.check_book_availability():
                book.set_book_availability(False)
                self.borrowed_books.append(book)
                print(f"Book Borrowed Successfully.")
                return
            elif book.isbn == book_id and book.check_book_availability() == False:
                print("Book borrowed by someone. Not Available!")
                return
        print("Book not found.")

    def return_book(self, book_id, library):
        for book in library:
            if book.isbn == book_id and not book.check_book_availability():
                book.set_book_availability(True)
                self.borrowed_books.remove(book)
                print(f"Book Returned Successfully.")
                return
        print("Book not found.")

    def save_borrowed_books(self):
        isbns = []
        for n in self.borrowed_books:
            isbns.append(n.isbn)
        with open(f"{self.name}.json", "w") as file:
            json.dump(isbns, file)

    def load_borrowed_books(self, library):
        filename = f"{self.name}.json"

        if not os.path.exists(filename):
            return

        if os.path.getsize(filename) == 0:
            return

        try:
            with open(filename, "r") as file:
                borrowed_books_isbns = json.load(file)  # List of ISBNs

            for bk_id in borrowed_books_isbns:
                for bk in library:
                    if bk.isbn == bk_id:
                        self.borrowed_books.append(bk)

        except json.JSONDecodeError:
            print(f"Warning: Borrowed books file '{filename}' is corrupted.")

    def total_borrowed_books(self):
        if len(self.borrowed_books) == 0:
            print("No Book Borrowed.")
        else:
            for b in self.borrowed_books:
                print(f"Title : {b.title}")
                print(f"Author : {b.author}")
                print(f"ISBN : {b.isbn}")


if __name__ == "__main__":

    members = []
    admins = []
    librarians = []

    library = []  # Stores all books

    # Create some users
    admin = Admin("Atta", "kingatta5464@gmail.com", "11", "atta5464")
    admins.append(admin)

    librarian1 = Librarian("Bob", "bob@example.com", "20", "libpass")
    librarian2 = Librarian("Watmor", "watmor@example.com", "21", "watmorpass")
    librarians.append(librarian1)
    librarians.append(librarian2)

    member1 = Member("Charlie", "charlie@example.com", "30", "charliepass")
    member2 = Member("Caroline", "caroline@example.com", "31", "carolinepass")
    members.append(member1)
    members.append(member2)

    # book1 = Book("Python Basics", "John Doe", "123")
    # book2 = Book("Data Science 101", "Jane Smith", "456")
    # book3 = Book("Machine Learning Essentials", "Tom Brown", "789")
    # book4 = Book("Artificial Intelligence Guide", "Sarah Connor", "321")
    # book5 = Book("Deep Learning with Python", "Francois Chollet", "654")
    # book6 = Book("Clean Code", "Robert C. Martin", "987")
    # book7 = Book("Algorithms Unlocked", "Thomas H. Cormen", "741")
    # book8 = Book("Database Management Systems", "Raghu Ramakrishnan", "852")
    # book9 = Book("The Pragmatic Programmer", "Andrew Hunt", "963")
    # book10 = Book("Fluent Python", "Luciano Ramalho", "159")

    # library.append(book1)
    # library.append(book2)
    # library.append(book3)
    # library.append(book4)
    # library.append(book5)
    # library.append(book6)
    # library.append(book7)
    # library.append(book8)
    # library.append(book9)
    # library.append(book10)

    # admin.write_book_data(library)
    library = admin.get_book_data()
    while True:
        print("=== Welcome to the Library Management System ===\n")
        print("1. Login as Admin\n")
        print("2. Login as Librarian\n")
        print("3. Login as Member\n")
        print("4. Exit\n")
        while True:
            choice = input("Enter your choice : ")
            if choice.isdigit():
                choice = int(choice)
            else:
                print("Input is not numeric... Try Again!")
                continue
            if choice < 1 or choice > 4:
                print("Number not in range 1-4. Try Again!")
            else:
                break

        if choice == 1:
            print("You have to enter Admin id and password to login.")
            id = input("Enter id : ")
            password = input("Enter password : ")
            logged_in = False

            for ad in admins:
                if ad.login(password, id) == True:
                    logged_in = True
                    while True:
                        print(f"You are logged in as Admin '{ad.name}'.\n")
                        print("What do you want?")
                        print("1. Add Book")
                        print("2. Remove Book")
                        print("3. View Details")
                        print("4. All Members Details")
                        print("5. Log Out")

                        while True:
                            c = input("Enter your choice : ")
                            if c.isdigit():
                                c = int(c)
                            else:
                                print("Input is not numeric... Try Again!")
                                continue
                            if c < 1 or c > 5:
                                print("Number not in range 1-5. Try Again!")
                            else:
                                break
                        if c == 1:
                            title = input("Enter book Title : ")
                            author = input("Enter book Author : ")
                            ISBN = input("Enter book ISBN : ")
                            b = Book(title, author, ISBN)
                            ad.add_book(library, b)
                        elif c == 2:
                            isbn = input("Eneter Book ISBN You want to remove : ")
                            ad.remove_book(library, isbn)
                        elif c == 3:
                            ad.view_reports(library)
                        elif c == 4:
                            ad.all_members_Details(members, library)
                        elif c == 5:
                            print("Logging Out as Admin...")
                            ad.write_book_data(library)
                            ad.logout()
                            break
            if not logged_in:
                print("Wrong Admin Id or Password")

        elif choice == 2:
            print("You have to enter Librarian id and password to login.")
            id = input("Enter id : ")
            password = input("Enter password : ")
            librarian_logged_in = False
            for l in librarians:
                if l.userid == id and l.get_password() == password:
                    librarian_logged_in = True
                    while True:
                        print(f"You are Logged In as Librarian {l.name}")
                        print("What do you want?")
                        print("1. View Books")
                        print("2. Search Book")
                        print("3. Issue Book")
                        print("4. Return Book")
                        print("5. Log Out")
                        while True:
                            c = input("Enter your choice : ")
                            if c.isdigit():
                                c = int(c)
                            else:
                                print("Input is not numeric... Try Again!")
                                continue
                            if c < 1 or c > 5:
                                print("Number not in range 1-5. Try Again!")
                            else:
                                break
                        if c == 1:
                            l.view_books(library)
                        elif c == 2:
                            id = input("Enter UserId of Book you want to search : ")
                            l.search_books(id, library)
                        elif c == 3:
                            id = input("Enter Book ISBN : ")
                            mem_id = input(
                                "Enter Member UserId Whom Book being issued : "
                            )
                            for m in members:
                                if m.userid == mem_id:
                                    l.issue_book(id, library, m)
                                    break
                            else:
                                print("No member have this UserId.")
                                continue
                        elif c == 4:
                            id = input("Enter Book ISBN : ")
                            mem_id = input(
                                "Enter Member UserId who is returning book : "
                            )
                            m_id = False
                            for m in members:
                                if m.userid == mem_id:
                                    l.return_book(id, library, m)
                                    m_id = True
                                    break
                            if not m_id:
                                print("No member have this UserId.")
                                continue
                        elif c == 5:
                            print("Loging Out as Librarian...")
                            l.write_book_data(library)
                            l.logout()
                            break

            if not librarian_logged_in:
                print("Wrong Librarian Id or Password")

        elif choice == 3:
            print("You have to enter Member id and password to login.")
            id = input("Enter id : ")
            password = input("Enter password : ")
            found_member = False
            for m in members:
                if m.userid == id and m.get_password() == password:
                    m.load_borrowed_books(library)
                    found_member = True
                    while True:
                        print(f"You are Logged In as Member {m.name}")
                        print("What do you want?")
                        print("1. View Books")
                        print("2. Search Book")
                        print("3. Borrow Book")
                        print("4. Return Book")
                        print("5. View Total Borrowed Books")
                        print("6. Log out")
                        while True:
                            c = input("Enter your choice : ")
                            if c.isdigit():
                                c = int(c)
                            else:
                                print("Input is not numeric... Try Again!")
                                continue
                            if c < 1 or c > 6:
                                print("Number not in range 1-6. Try Again!")
                            else:
                                break
                        if c == 1:
                            m.view_books(library)
                        elif c == 2:
                            id = input("Enter UserId of Book you want to search : ")
                            m.search_books(id, library)
                        elif c == 3:
                            id = input("Enter Book ISBN : ")
                            m.borrow_book(id, library)
                        elif c == 4:
                            id = input("Enter Book ISBN : ")
                            m.return_book(id, library)
                        elif c == 5:
                            m.total_borrowed_books()
                        elif c == 6:
                            print("Loging Out as Member...")
                            m.write_book_data(library)
                            m.save_borrowed_books()
                            m.logout()
                            break
            if not found_member:
                print("No member has this UserId.")
        elif choice == 4:
            admin.write_book_data(library)
            print("Exiting Program.")

            exit()
