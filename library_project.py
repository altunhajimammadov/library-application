import sqlite3
import time

class Book():

    def __init__(self, name, writer, publisher, type, printing):
        self.name = name
        self.writer = writer
        self.publisher = publisher
        self.type = type
        self.printing = printing

    def __str__(self):
        return """

        BOOK NAME: {}

        BOOK WRITER: {}

        BOOK PUBLISHER: {}

        BOOK TYPE: {}

        NUMBERS OF BOOK: {}

        """.format(self.name, self.writer, self.publisher, self.type, self.printing)

class Member():

    def __init__(self, name, surname, date_of_bird, phone_number, book_debt):
        self.name = name
        self.surname = surname
        self.date_of_bird = date_of_bird
        self.phone_number = phone_number
        self.book_debt = book_debt

    def __str__(self):
        return """

        NAME: {}

        SURNAME: {}

        DATE OF BIRD: {}

        PHONE NUMBER: {}

        NUMBER OF BOOKS OWED: {}

        """.format(self.name, self.surname, self.date_of_bird, self.phone_number, self.book_debt)

class Library():

    def __init__(self):

        self.create_connection()
        self.create_connection_member()

    def create_connection(self):

        self.connection = sqlite3.connect("library.db")
        self.cursor = self.connection.cursor()

        query = "Create table if not exists books (NAME TEXT,WRITER TEXT,PUBLISHER TEXT,TYPE TEXT,PRINTING INT)"
        self.cursor.execute(query)
        self.connection.commit()

    def create_connection_member(self):

        self.user_connection = sqlite3.connect("member.db")
        self.user_cursor = self.user_connection.cursor()

        query = "Create table if not exists members (NAME TEXT,SURNAME TEXT,DATE_OF_BİRD TEXT,PHONE_NUMBER INT,BOOK_DEBT INT)"
        self.user_cursor.execute(query)
        self.user_connection.commit()

    def disconnect_connection(self):
        self.connection.close()

    def disconnect_connection_member(self):
        self.user_connection.close()

    def show_books(self):

        query = "Select * from books"
        self.cursor.execute(query)

        book_list = self.cursor.fetchall()

        if (len(book_list) == 0):
            print("Unfortunately there is not any book in the library...")

        else:
            for i in book_list:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)

    def book_inquiry(self, name):
        query = "Select * From books where name = ?"

        self.cursor.execute(query, (name,))
        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("Please wait, the book is searching...")
            time.sleep(2)
            print("There is not any book, that it's name is {}".format(name))
            return "0"  # Write this to check that the book exists.(function: borrow_book,delete_book)

        else:

            book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])

            print("Please wait, the book is searching...")
            time.sleep(2)
            print(book)
            return "1"  # Write this to check that the book exists.(function: borrow_book,delete_book)

    def add_book(self, book):
        query = "Insert Into books Values(?,?,?,?,?)"

        self.cursor.execute(query, (book.name, book.writer, book.publisher, book.type, book.printing))
        self.connection.commit()

    def delete_book(self, name):
        query = "Delete from books where name = ?"

        self.cursor.execute(query, (name,))
        self.connection.commit()

    def upgrade_book_number(self, name):

        query = "Select * from books where name = ?"

        self.cursor.execute(query, (name,))
        book = self.cursor.fetchall()

        if (len(book) == 0):
            print("Please wait, the book is searching...")
            time.sleep(2)
            print("There is not any book, that it's name is {}".format(name))
        else:
            print("Please wait, the book is searching...")
            time.sleep(1)
            number = int(input("How many books, named '{}' will be added to the library? : ".format(name)))

            prints = book[0][4]
            prints += number

            query2 = "Update books set printing = ? where name = ?"

            self.cursor.execute(query2, (prints, name))
            self.connection.commit()

            print("The book was found and the number of book was upgraded")

    def upgrade_book_number_automatic(self, name):

        query = "Select * from books where name = ?"

        self.cursor.execute(query, (name,))
        book = self.cursor.fetchall()

        prints = book[0][4]
        prints += 1

        query2 = "Update books set printing = ? where name = ?"

        self.cursor.execute(query2, (prints, name))
        self.connection.commit()

    def borrow_book(self, book_name, cust_name):

        query = "Select * from members where name = ?"
        query1 = "Select * from books where name = ?"
        query2 = "Update books set printing = ? where name = ?"
        query3 = "Update members set book_debt = ? where name = ?"

        self.cursor.execute(query1, (book_name,))
        book = self.cursor.fetchall()

        prints = book[0][4]
        prints -= 1

        if prints < 0:
            print("Unfortunately, this book is currently out of stock in the library.")

        else:

            self.cursor.execute(query2, (prints, book_name))
            self.connection.commit()

            self.user_cursor.execute(query, (cust_name,))
            member = self.user_cursor.fetchall()

            debt_number = member[0][4]
            debt_number += 1

            self.user_cursor.execute(query3, (debt_number, cust_name))
            self.user_connection.commit()

    def return_book(self, book_name, cust_name):
        query = "Select * from members where name = ?"
        query1 = "Select * from books where name = ?"
        query2 = "Update books set printing = ? where name = ?"
        query3 = "Update members set book_debt = ? where name = ?"

        self.cursor.execute(query1 , (book_name,))
        book = self.cursor.fetchall()

        prints = book[0][4]
        prints += 1

        self.cursor.execute(query2, (prints, book_name))
        self.connection.commit()

        self.user_cursor.execute(query, (cust_name,))
        member = self.user_cursor.fetchall()

        debt_number = member[0][4]
        debt_number -= 1

        self.user_cursor.execute(query3, (debt_number, cust_name))
        self.user_connection.commit()

    def show_members(self):
        query = "Select * from members"

        self.user_cursor.execute(query)
        member_list = self.user_cursor.fetchall()

        if (len(member_list) == 0):
            print("Unfortunately, there is not any member in the library.")

        else:
            for i in member_list:
                member = Member(i[0],i[1],i[2],i[3],i[4])
                print(member)

    def add_member(self, member):
        query = "Insert Into members Values(?,?,?,?,?)"

        self.user_cursor.execute(query, (
        member.name, member.surname, member.date_of_bird, member.phone_number, member.book_debt))
        self.user_connection.commit()

    def delete_member(self, name):
        query = "Delete from members where name = ?"

        self.user_cursor.execute(query, (name,))
        self.user_connection.commit()

    def member_inquiry(self, name):
        query = "Select * From members where name = ?"

        self.user_cursor.execute(query, (name,))
        members = self.user_cursor.fetchall()

        if (len(members) == 0):
            print("Please wait, the member is searching...")
            time.sleep(2)
            print("There is not any member, that he/she name is {}.".format(name))
            return "0"  # Write this to check that the book exists.(function: borrow_book, delete_member)

        else:
            member = Member(members[0][0], members[0][1], members[0][2], members[0][3], members[0][4])

            print("Please wait, the member is searching...")
            time.sleep(2)
            print(member)
            return "1"  # Write this to check that the book exists.(function: borrow_book, delete_member)
          
