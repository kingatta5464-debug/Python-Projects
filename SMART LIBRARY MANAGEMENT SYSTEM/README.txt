========================
Library Management System
========================

Project Overview:
-----------------
This is a Python-based Library Management System that allows Admins, Librarians, and Members 
to manage and use library resources. It uses Object-Oriented Programming principles 
(inheritance, abstraction, encapsulation) and JSON file storage to persist data.

Key Features:
-------------
1. **Multiple Roles**:
   - Admin: Can add/remove books, view reports, see all members' details.
   - Librarian: Can view/search books, issue books to members, and accept returns.
   - Member: Can view/search books, borrow and return books, and check their borrowed books.

2. **Persistent Storage**:
   - Books and borrowed book data are saved in JSON files (`books_data.json` and `<MemberName>.json`).
   - Data is automatically loaded on program start and saved on logout.

3. **Book Management**:
   - Add new books with title, author, and ISBN.
   - Remove books using ISBN.
   - Track availability of books (Available/Unavailable).

4. **Borrowing System**:
   - Librarians and Members can borrow and return books.
   - System prevents double borrowing of unavailable books.

5. **User Authentication**:
   - Each user (Admin, Librarian, Member) logs in with a User ID and password.
   - Basic authentication logic is implemented for role-based access.

Technologies Used:
------------------
- Python (OOP concepts: classes, inheritance, abstraction, encapsulation)
- JSON (for data storage)
- File Handling (reading and writing data)
- Command-line interface (CLI)

Project Structure:
------------------
- `books_data.json`  → Stores library book data
- `<MemberName>.json` → Stores borrowed books for each member
- `library_management.py` → Main source code file

How to Run:
-----------
1. Make sure you have Python 3 installed.
2. Save all files in the same folder.
3. Open a terminal/command prompt in that folder.
4. Run:
5. Use the menu to log in as Admin, Librarian, or Member and perform actions.

Example Login Credentials (Default):
------------------------------------
- Admin:
 ID: 11
 Password: atta5464
- Librarians:
 1. ID: 20 | Password: libpass
 2. ID: 21 | Password: watmorpass
- Members:
 1. ID: 30 | Password: charliepass
 2. ID: 31 | Password: carolinepass

Notes:
------
- Make sure to log out properly to save changes to the JSON files.
- If `books_data.json` does not exist, you may need to add books first as an Admin.
- This program runs in the terminal and uses numeric menu inputs for navigation.

Author:
-------
Atta Ul Mustafa
