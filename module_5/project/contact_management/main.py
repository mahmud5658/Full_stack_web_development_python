from file_operations import save_contact, load_contact
from cli_menu import display_menu, get_user_choice
from contact import Contact
from functions import add_contact, view_contact,remove_contact,search_contact


def main():
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contact()
        elif choice==3:
            remove_contact()
        elif choice == 4:
            search_contact()
        elif choice == 5:
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid input. Please enter a number between 1 and 5")

if __name__ == "__main__":
    main()
