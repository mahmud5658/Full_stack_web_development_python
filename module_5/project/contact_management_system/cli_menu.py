def display_menu():
    print("\nContact Book Menu\n")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")


def get_user_choice():
    try:
        return int(input("\nEnter your choice: "))
    except ValueError:
        print("\nInvalid input. Please enter a number between 1 and 5")
        return None
