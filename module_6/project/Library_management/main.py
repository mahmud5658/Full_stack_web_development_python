import datetime
from lend_manager import view_lended_books, lend_book, return_book
from tabulate import tabulate
from book_manager import load_books

from book_manager import (
    check_book_availability,
    update_book_quantity,
    load_books,
    save_books,
)

def display_menu():
    print("1. View Books")
    print("2. Add Book")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. View Lent Books")
    print("6. Exit")


def view_books():
    books = load_books()

    book_data = []
    for book in books:
        book_data.append([book["title"], book["quantity"]])

    print(
        "\n"
        + tabulate(book_data, headers=["Book Title", "Quantity"], tablefmt="fancy_grid")
    )


def add_book():
    title = input("Enter book title: ")
    quantity = int(input("Enter quantity: "))

    books = load_books()
    books.append({"title": title, "quantity": quantity})
    save_books(books)
    print(f"Book '{title}' added with quantity {quantity}.")


def lend_book_function():
    book_title = input("Enter the book title to lend: ")

    if check_book_availability(book_title):
        borrower_name = input("Enter borrower's name: ")
        borrower_phone = input("Enter borrower's phone number: ")
        return_due_date = input("Enter return due date (YYYY-MM-DD): ")


        due_date = lend_book(book_title, borrower_name, borrower_phone, return_due_date)

        update_book_quantity(book_title, -1)
        print(
            f"The book '{book_title}' has been lent to {borrower_name}. Due date: {due_date.strftime('%Y-%m-%d')}"
        )
    else:
        print("There are not enough books available to lend.")


def return_book_function():
    book_title = input("Enter the book title to return: ")

    return_book(book_title)


    update_book_quantity(book_title, 1)
    print(f"The book '{book_title}' has been returned successfully.")


def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            lend_book_function()
        elif choice == "4":
            return_book_function()
        elif choice == "5":
            view_lended_books()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
