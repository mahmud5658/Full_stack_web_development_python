import json

file_path1 = "module_6\project\Library_management\database\\books.json"
def load_books():
    try:
        with open(file_path1, "r"
        ) as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_books(books):
    with open(file_path1, "w") as file:
        json.dump(books, file, indent=4)


def check_book_availability(book_title):
    books = load_books()
    for book in books:
        if book["title"] == book_title and book["quantity"] > 0:
            return True
    return False


def update_book_quantity(book_title, change):
    books = load_books()
    for book in books:
        if book["title"] == book_title:
            book["quantity"] += change
    save_books(books)
