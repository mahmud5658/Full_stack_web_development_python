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
            raise ValueError("\nPhone number must be numeric.")
    except ValueError as e:
        print(f"Error: {e}")

    for contact in contacts:
        if contact["phone"] == phone:
            print("\nA contact with this number already exists.")
            return
    contact = Contact(name, email, phone, address)
    new_contact = contact.to_json()
    contacts.append(new_contact)
    save_contact(contacts)
    print("\nNew contact added successfully!")


def view_contact():
    contacts = load_contact()
    if not contacts:
        print("\nNo contact available!")
        return
    print(f"{'Name':<30} {'Email':<30} {'Phone':<30} {'Address':<30}")
    print("-" * 110)
    for contact in contacts:
        print(
            f"{contact['name']:<30} {contact['email']:<30} {contact['phone']:<30} {contact['address']:<30}"
        )


def remove_contact():
    contacts = load_contact()
    phone = input("\nEnter the phone number of the contact to remove: ").strip()
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contact(contacts)
            print("\nContact remove successfully!")


def search_contact():
    """Search for a contact by name, email, or phone."""
    contacts = load_contact()
    search_term = input("\nEnter name, email, or phone to search: ").strip().lower()
    results = []
    if isinstance(contacts, list):
        for contact in contacts:
            if (
                search_term in contact.get("name", "").lower()
                or search_term in contact.get("email", "").lower()
                or search_term in contact.get("phone", "").lower()
            ):
                results.append(contact)

    if results:
        print("\nSearch Results:")
        print(f"{'Name':<30} {'Email':<30} {'Phone':<30} {'Address':<30}")
        print("-" * 120)
        for contact in results:
            print(
                f"{contact.get('name', 'N/A'):<30} "
                f"{contact.get('email', 'N/A'):<30} "
                f"{contact.get('phone', 'N/A'):<30} "
                f"{contact.get('address', 'N/A'):<30}"
            )
    else:
        print("\nNo matching contacts found.")
