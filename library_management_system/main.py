from Book import Book
from Member import Member
from Library import Library
library=Library()

print("Welcome To Library Management System")
is_operation = True

while is_operation:

    user_operation = input(
        "\nD=Display, B=Borrow, R=Return, M=Register, E=Exit\n"
        "Enter operation: "
    )

    if user_operation == "D":
        library.display_available_books()

    elif user_operation == "B":
        memberID = int(input("Enter Your Member ID: "))
        bookTitle = input("Enter the title of book to issue: ")
        library.issue_book(memberID, bookTitle)

    elif user_operation == "R":
        memberID = int(input("Enter Your Member ID: "))
        bookTitle = input("Enter the title of book to return: ")
        library.accept_return(memberID, bookTitle)

    elif user_operation == "M":
        member_name = input("Enter your name: ")

    elif user_operation == "E":
        is_operation = False