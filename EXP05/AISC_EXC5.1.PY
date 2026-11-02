members = ["soham", "suyash", "saurabh", "durva", "zeel"]

books = ["Python", "AI", "Database"]

authors = {"Python": "Guido", "AI": "Russell", "Database": "Korth"}

available = ["Python", "Database"]

borrowed = []

books_issued_count = {}

membership_expired = []


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

    print("\nBooks Issued Count:")
    for member, count in books_issued_count.items():
        print("BooksIssued(", member, ",", count, ")")

    print("\nMembership Expired:")
    if len(membership_expired) == 0:
        print("No expired memberships.")
    else:
        for member in membership_expired:
            print("MembershipExpired(", member, ")")


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

    for member, count in books_issued_count.items():

        if count > 3:
            print("BorrowingLimitExceeded(", member, ")")

    for member in membership_expired:
        print("BorrowingDenied(", member, ")")


def add_member():

    name = input("Enter member name: ")

    if name in members:
        print("Member already exists.")
    else:
        members.append(name)
        books_issued_count[name] = 0
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

    if member in membership_expired:
        print("Membership expired. Borrowing denied.")
        return

    if book not in books:
        print("Book does not exist.")
        return

    if book not in available:
        print("Book is not available.")
        return

    borrowed.append((member, book))
    available.remove(book)

    books_issued_count[member] = books_issued_count.get(member, 0) + 1

    print(member, "borrowed", book)

    if books_issued_count[member] > 3:
        print("Warning: BorrowingLimitExceeded(", member, ")")


def return_book():

    member = input("Enter member name: ")
    book = input("Enter book title: ")

    if (member, book) not in borrowed:
        print("Borrowing record not found.")
        return

    borrowed.remove((member, book))
    available.append(book)

    if member in books_issued_count and books_issued_count[member] > 0:
        books_issued_count[member] -= 1

    print(book, "has been returned.")


def expire_membership():

    member = input("Enter member name: ")

    if member not in members:
        print("Member does not exist.")
        return

    if member in membership_expired:
        print("Membership already expired.")
        return

    membership_expired.append(member)
    print("Membership of", member, "marked as expired.")


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
    print("MembershipExpired Rahul")

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

    elif predicate == "MembershipExpired":

        if value in membership_expired:
            print("TRUE")
        else:
            print("FALSE")

    elif predicate == "BorrowingLimitExceeded":

        if books_issued_count.get(value, 0) > 3:
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
    print("10. Expire Membership")
    print("11. Run Inference")
    print("12. Exit")

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
        expire_membership()

    elif choice == "11":
        infer()

    elif choice == "12":
        print("\nThank you for using the FOL Library System!")
        break

    else:
        print("Invalid choice. Please try again.")
