# Contact Management System
contacts = [] 

def show_menu():
    print("\n====== CONTACT MANAGEMENT SYSTEM ======")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!")


def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found!")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")


def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone number to search: ")

    found = False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("No matching contact found.")


def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Leave blank if you don't want to change a field.")

            new_phone = input("New Phone (press Enter to skip): ")
            new_email = input("New Email (press Enter to skip): ")
            new_address = input("New Address (press Enter to skip): ")

            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


# ---- Main Program Loop ----
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice!")
