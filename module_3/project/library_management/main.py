import json

DATA_FILE = "module_3/project/library_management/database/books.json"


def load_books():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(DATA_FILE, "w") as file:
        json.dump(books, file, indent=4)


def add_book():
    title = input("Enter book title: ")
    authors = input("Enter author(s) (comma-separated): ")
    isbn = input("Enter ISBN: ")
    year = input("Enter publishing year: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    books = load_books()

    for book in books:
        if book["ISBN"] == isbn:
            print("Book with this ISBN already exists!")
            return

    new_book = {
        "Title": title,
        "Authors": authors,
        "ISBN": isbn,
        "Year": year,
        "Price": price,
        "Quantity": quantity,
    }
    books.append(new_book)
    save_books(books)
    print("Book added successfully!")

def view_books():
    books = load_books()
    if not books:
        print("No books available.")
        return
    print(
        f"{'Title':<30} {'Authors':<20} {'ISBN':<15} {'Year':<6} {'Price':<8} {'Qty':<5}"
    )
    print("-" * 90)
    for book in books:
        print(
            f"{book['Title']:<30} {book['Authors']:<20} {book['ISBN']:<15} {book['Year']:<6} {book['Price']:<8.2f} {book['Quantity']:<5}"
        )


def update_book():
    isbn = input("Enter ISBN of the book to update: ")
    books = load_books()

    for book in books:
        if book["ISBN"] == isbn:
            print("Book found! Leave fields empty to retain current values.")
            book["Title"] = input(f"New Title ({book['Title']}): ") or book["Title"]
            book["Authors"] = (
                input(f"New Authors ({book['Authors']}): ") or book["Authors"]
            )
            book["Year"] = input(f"New Year ({book['Year']}): ") or book["Year"]
            book["Price"] = float(
                input(f"New Price ({book['Price']}): ") or book["Price"]
            )
            book["Quantity"] = int(
                input(f"New Quantity ({book['Quantity']}): ") or book["Quantity"]
            )
            save_books(books)
            print("Book updated successfully!")
            return
    print("Book not found.")

def remove_book():
    isbn = input("Enter ISBN of the book to remove: ")
    books = load_books()

    for book in books:
        if book["ISBN"] == isbn:
            books.remove(book)
            save_books(books)
            print("Book removed successfully!")
            return
    print("Book not found.")


# Main menu
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Remove Book")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            remove_book()
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
