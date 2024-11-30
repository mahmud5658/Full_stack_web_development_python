from contact import Contact
from file_operations import save_contact, load_contact


def add_contact():
    contacts = load_contact()
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone: ").strip()
    address = input("Enter Address: ").strip()

    try:
        if not phone.isdigit():
            raise ValueError("Phone number must be numeric.")
    except ValueError as e:
        print(f"Error: {e}")

    for contact in contacts:
        if contact["phone"] == phone:
            print("A contact with this number already exists.")
            return
    contact = Contact(name, email, phone, address)
    new_contact = contact.to_json()
    contacts.append(new_contact)
    save_contact(contacts)
    print("\nNew contact added successfully!")



