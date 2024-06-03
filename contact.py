class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added.")
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")
    def search_contact(self, search_term):
        results = [
            contact for contact in self.contacts
            if search_term.lower() in contact.name.lower() or search_term in contact.phone
        ]
        if not results:
            print(f"No contacts found for '{search_term}'.")
        else:
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
    def update_contact(self, old_name, new_name=None, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == old_name.lower():
                if new_name:
                    contact.name = new_name
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"Contact '{old_name}' updated.")
                return
        print(f"Contact '{old_name}' not found.")
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted.")
                return
        print(f"Contact '{name}' not found.")
def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")    
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter postal address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name (or press Enter to keep the same): ")
            new_phone = input("Enter new phone number (or press Enter to keep the same): ")
            new_email = input("Enter new email (or press Enter to keep the same): ")
            new_address = input("Enter new address (or press Enter to keep the same): ")
            contact_book.update_contact(old_name, new_name or None, new_phone or None, new_email or None, new_address or None)
        elif choice == "5":
            name_to_delete = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name_to_delete)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
