import json
import datetime
from tabulate import tabulate

file_path2 = "module_6\project\Library_management\database\lend_books.json"
def load_lend_books():
    try:
        with open(file_path2, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_lend_books(lend_books):
    with open(file_path2, "w") as file:
        json.dump(lend_books, file, indent=4)


def lend_book(book_title, borrower_name, borrower_phone, return_due_date):
    lend_books = load_lend_books()


    due_date = datetime.datetime.strptime(return_due_date, "%Y-%m-%d")

    lend_books.append(
        {
            "borrower_name": borrower_name,
            "borrower_phone": borrower_phone,
            "book_title": book_title,
            "due_date": due_date.strftime("%Y-%m-%d"),
        }
    )
    save_lend_books(lend_books)
    return due_date


def return_book(book_title):
    lend_books = load_lend_books()
    lend_books = [lend for lend in lend_books if lend["book_title"] != book_title]
    save_lend_books(lend_books)


def view_lended_books():
    lend_books = load_lend_books()

    lend_data = []
    for lend in lend_books:
        lend_data.append(
            [
                lend["borrower_name"],
                lend["borrower_phone"],
                lend["book_title"],
                lend["due_date"],
            ]
        )

    print(
        "\n"
        + tabulate(
            lend_data,
            headers=["Borrower Name", "Phone Number", "Book Title", "Due Date"],
            tablefmt="fancy_grid",
        )
    )
