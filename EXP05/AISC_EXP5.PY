members = ["Rahul", "Priya"]

books = ["Python", "AI", "Database"]

authors = {"Python": "Guido", "AI": "Russell", "Database": "Korth"}

available = ["Python", "Database"]

borrowed = []


def display_kb():

    print("\n========== KNOWLEDGE BASE ==========")

    print("\nMembers:")
    for member in members:
        print("Member(", member, ")")

    print("\nBooks:")
    for book in books:
        print("Book(", book, ")")

    print("\nAuthors:")
    for book, author in authors.items():
        print("WrittenBy(", book, ",", author, ")")

    print("\nAvailable Books:")
    for book in available:
        print("Available(", book, ")")

    print("\nBorrowed Books:")

    if len(borrowed) == 0:
        print("No books borrowed.")
    else:
        for member, book in borrowed:
            print("Borrows(", member, ",", book, ")")


def infer():

    print("\n========== FOL INFERENCE ==========")

    for member, book in borrowed:

        if member in members:
            print("Borrower(", member, ")")

    for book in books:

        if book in available:
            print("CanBorrow(", book, ")")

    for book, author in authors.items():

        if book in books:
            print("HasAuthor(", book, ",", author, ")")


def add_member():

    name = input("Enter member name: ")

    if name in members:
        print("Member already exists.")
    else:
        members.append(name)
        print("Member added successfully.")


def add_book():

    title = input("Enter book title: ")
    author = input("Enter author name: ")

    if title in books:
        print("Book already exists.")
        return

    books.append(title)
    authors[title] = author
    available.append(title)

    print("Book added successfully.")


def borrow_book():

    member = input("Enter member name: ")
    book = input("Enter book title: ")

    if member not in members:
        print("Member does not exist.")
        return

    if book not in books:
        print("Book does not exist.")
        return

    if book not in available:
        print("Book is not available.")
        return

    borrowed.append((member, book))
    available.remove(book)

    print(member, "borrowed", book)


def return_book():

    member = input("Enter member name: ")
    book = input("Enter book title: ")

    if (member, book) not in borrowed:
        print("Borrowing record not found.")
        return

    borrowed.remove((member, book))
    available.append(book)

    print(book, "has been returned.")


def check_book():

    book = input("Enter book title: ")

    if book not in books:
        print("Book does not exist.")
        return

    if book in available:
        print(book, "is AVAILABLE.")
    else:
        print(book, "is NOT AVAILABLE.")


def find_author():

    book = input("Enter book title: ")

    if book in authors:
        print("Author of", book, "is", authors[book])
    else:
        print("Book not found.")


def show_borrowed():

    member = input("Enter member name: ")

    found = False

    print("\nBorrowed Books:")

    for m, book in borrowed:

        if m == member:
            print("-", book)
            found = True

    if not found:
        print("No books borrowed.")


def query_fol():

    print("\n========== FOL QUERY ==========")

    print("Examples:")
    print("Member Rahul")
    print("Book Python")
    print("Available Python")

    predicate = input("\nEnter predicate: ")
    value = input("Enter value: ")

    if predicate == "Member":

        if value in members:
            print("TRUE")
        else:
            print("FALSE")

    elif predicate == "Book":

        if value in books:
            print("TRUE")
        else:
            print("FALSE")

    elif predicate == "Available":

        if value in available:
            print("TRUE")
        else:
            print("FALSE")

    elif predicate == "Borrower":

        found = False

        for member, book in borrowed:

            if member == value:
                found = True

        if found:
            print("TRUE")
        else:
            print("FALSE")

    else:
        print("Unknown predicate.")


while True:

    print("\n")
    print("========================================")
    print("       FOL LIBRARY MANAGEMENT SYSTEM")
    print("========================================")

    print("1. Add Member")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Check Book Availability")
    print("6. Find Book Author")
    print("7. Show Borrowed Books")
    print("8. FOL Query")
    print("9. Display Knowledge Base")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_member()

    elif choice == "2":
        add_book()

    elif choice == "3":
        borrow_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        check_book()

    elif choice == "6":
        find_author()

    elif choice == "7":
        show_borrowed()

    elif choice == "8":
        query_fol()

    elif choice == "9":
        display_kb()

    elif choice == "10":
        print("\nThank you for using the FOL Library System!")
        break

    else:
        print("Invalid choice. Please try again.")
