from mine_library_project import *

print("""
*************************************************

*\*/*\*/Welcome to Library Application\*/*\*/*

PROCESSES:

1. Show Books

2. Book Inquiry

3. Add Book

4. Delete Book

5. Borrowing Book

6. Returning Book

7. Upgrade the Number of Book

8. Show Members

9. Add Member

10. Delete Member

11. Member Inquiry

PRESS 'Q' TO EXIT!!!

IMPORTANT: Please enter all input's with capital letters.

*************************************************
""")

library = Library()
member = Library()

while True:
    process = input("Please enter the process number you want: ")

    if process == "Q":

        print("The application is closing...")
        time.sleep(2)
        print("\nHave a Nice Day!!!")
        break

    elif process == "1":

        library.show_books()

    elif process == "2":

        name = input("Enter the book's name: ")
        print("The book is currently being questioned...")
        time.sleep(2)
        library.book_inquiry(name)

    elif process == "3":

        try:
            print("Please enter information about the book you want to add.")
            time.sleep(1)
            name = input("Book Name: ")
            writer = input("Writer: ")
            publisher = input("Publisher: ")
            type = input("Type: ")
            print_number = int(input("Number of book: "))

            new_book = Book(name,writer,publisher,type,print_number)

            print("The book is being added to the library...")
            time.sleep(2)
            library.add_book(new_book)
            print("The book successfully added.")

        except ValueError:
            print("Number of Book can't be a string value, please try again.")

    elif process == "4":

        name_delete = input("Please enter the book's name you want to delete: ")
        delete_key = library.book_inquiry(name_delete)
        if delete_key == "0":
            continue

        else:
            answer = input("Are you sure you want to ^DELETE^ this book? Enter YES/NO: ")

            if answer == "YES":
                print("The book is being deleted...")
                time.sleep(2)
                library.delete_book(name_delete)
                print("The book was successfully deleted.")

            elif answer == "NO":
                print("deletion canceled!!!".upper())
                continue

            else:
                print("The answer you entered is not defined, please enter your answer with capital letters.")
                continue

    elif process == "5":

        while True:
            customer_name = input("Please enter the customer's name: ")
            key_cust = member.member_inquiry(customer_name)
            if key_cust == "0":
                time.sleep(2)
                print("If you are not a member, you cannot borrow books.")
                time.sleep(1)
                cust_answer = input("Would you like to be a member of the library? YES/NO : ")
                if cust_answer == "YES":
                    print("Please wait...")
                    time.sleep(1)
                    print("Please enter information about the you:")
                    cust_name = input("Name: ")
                    cust_surname = input("Surname: ")
                    cust_date_of_bird = input("Date of Bird - (dd/mm/yyyy) : ")
                    cust_phone_number = int(input("Phone Number: "))
                    cust_book_debt = 0

                    new_member = Member(cust_name,cust_surname,cust_date_of_bird,cust_phone_number,cust_book_debt)

                    print("The member is being registered...")
                    library.add_member(new_member)
                    time.sleep(2)
                    print("The member was successfully added.")
                    time.sleep(1)
                    print("Now you can borrow any book you want.")
                    time.sleep(1)

                    while True:

                        wanted_book = input("Please enter the wanted book's name: ")
                        key_book = library.book_inquiry(wanted_book)
                        time.sleep(1)
                        if key_book == "0":
                            brrw_answer = input("Would you like to inquire another book? YES/NO : ")
                            if brrw_answer == "YES":
                                print("Please wait...")
                                time.sleep(1)
                                continue
                            elif brrw_answer == "NO":
                                print("Please wait, you are directed to the main menu...")
                                time.sleep(1)
                                break
                            else:
                                print("The answer you entered is not defined, enter your answer with capital letters, you are directed to the main menu...")
                                time.sleep(2)
                                break
                        elif key_book == "1":
                            book_answer = input("Is this book you wanted? YES/NO: ")
                            if book_answer == "YES":
                                library.borrow_book(wanted_book, customer_name)
                                print("Please wait...")
                                time.sleep(1)
                                print("Borrowing process was successfully completed.")
                                break

                            elif book_answer == "NO":
                                print("There is not another book in the library which name is {}.".format(wanted_book))
                                break
                            else:
                                print("The answer you entered is not defined, enter your answer with capital letters, you are directed to the main menu...")
                                break
                    break

                elif cust_answer == "NO":
                    print("Please wait, you are directed to the main menu...")
                    time.sleep(1)
                    break

                else:
                    print("The answer you entered is not defined, enter your answer with capital letters,you are directed to the main menu...")
                    time.sleep(2)
                    break
            else:
                while True:

                    wanted_book = input("Please enter the book name the customer want: ")
                    key_book = library.book_inquiry(wanted_book)
                    time.sleep(1)
                    if key_book == "0":
                        brrw_answer = input("Would you like to inquire another book? YES/NO : ")
                        if brrw_answer == "YES":
                            print("Please wait...")
                            time.sleep(1)
                            continue
                        elif brrw_answer == "NO":
                            print("Please wait, you are directed to the main menu...")
                            time.sleep(1)
                            break
                        else:
                            print("The answer you entered is not defined, enter your answer with capital letters, you are directed to the main menu...")
                            time.sleep(2)
                            break
                    elif key_book == "1":
                        book_answer = input("Is this book you wanted? YES/NO: ")
                        if book_answer == "YES":
                            library.borrow_book(wanted_book, customer_name)
                            print("Please wait...")
                            time.sleep(1)
                            print("Borrowing process was successfully completed.")
                            break

                        elif book_answer == "NO":
                            print("There is not another book in the library which name is {}.".format(wanted_book))
                            break
                        else:
                            print("The answer you entered is not defined, enter your answer with capital letters, you are directed to the main menu...")
                            break
                break

    elif process == "6":

        try:
            returner_name = input("Please enter the customer's name: ")
            returner_wanted_book = input("Please enter the book's name the customer want to return: ")
            print("Please wait...")
            time.sleep(2)

            library.return_book(returner_wanted_book,returner_name)

            print("Returning process was successfully completed.")

        except IndexError:
            print("Entered Customer Name or Book Name is Wrong!")

    elif process == "7":

        name_upgrade = input("Please enter the book's name you want to upgrade it's number: ")
        library.upgrade_book_number(name_upgrade)

    elif process == "8":

        library.show_members()

    elif process == "9":

        print("Please enter some information about the member.")
        time.sleep(1)
        new_cust_name = input("Name: ")
        new_cust_surname = input("Surname: ")
        new_cust_date_of_bird = input("Date of Bird - (dd/mm/yyyy) : ")
        new_cust_phone_number = input("Phone Number: ")
        new_cust_book_debt = 0

        new_cust = Member(new_cust_name,new_cust_surname,new_cust_date_of_bird,new_cust_phone_number,new_cust_book_debt)

        print("Please wait, the member is being registered to the library...")
        library.add_member(new_cust)
        time.sleep(2)
        print("The member was successfully registered.")

    elif process == "10":

        member_name_delete = input("Please enter the member's name you want to delete: ")
        time.sleep(2)
        key_delete = library.member_inquiry(member_name_delete)
        if key_delete == "0":
            continue

        else:
            answer = input("Are you sure you want to ^DELETE^ this member? Enter YES/NO: ")

            if answer == "YES":
                print("The member is being deleted...")
                time.sleep(2)
                library.delete_member(member_name_delete)
                print("The member was successfully deleted.")

            elif answer == "NO":
                print("deletion canceled!!!".upper())
                continue

            else:
                print("The answer you entered is not defined, please enter your answer with capital letters.")
                continue

    elif process == "11":

        mbr_name = input("Please enter the member's name: ")
        print("The member is currently being questioned...")
        time.sleep(2)
        library.member_inquiry(mbr_name)

    else:
        print("PROCESS NUMBER IS NOT DEFINED!!!")
