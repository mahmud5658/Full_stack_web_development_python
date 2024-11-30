from file_operations import save_contact,load_contact
from cli_menu import display_menu,get_user_choice
from contact import Contact
from functions import add_contact


def main():
    while True:
        display_menu()
        choice = get_user_choice()
        if(choice==1):
            add_contact()


if __name__ == "__main__":
    main()