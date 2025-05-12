contacts = {}

def create_contact(contact_book):
    global Name
    global Phone
    Name = input("Enter your name: ")
    Phone = input("Enter your phone number: ")
    contact_book[Name] = Phone
    print(f"Contact '{Name}: {Phone}' has been added successfully!")

def view_contact(contact_book):
    global View_Name
    View_Name = input("Enter the name of the contact you want to view: ")
    if View_Name in contact_book:
        print(f"Contact '{View_Name}: {contact_book[View_Name]}' has been found successfully!")
    else:
        print(f"Contact '{View_Name}' not found in the contact book.")

def delete_contact(contact_book):
    global Delete_Name
    Delete_Name = input("Enter the name of the contact you want to delete: ")
    if Delete_Name in contact_book:
        del contact_book[Delete_Name]
        print(f"Contact '{Delete_Name}' has been deleted successfully!")
    else:
        print(f"Contact '{Delete_Name}' not found in the contact book.")

def view_all_contacts(contact_book):
    if not contact_book:
        print("No contacts found in the contact book!")
    else:
        print("\nAll Contacts:")
        for name, phone in contact_book.items():
            print(f"Name: {name}, Phone: {phone}")

def display_menu():
    print("Welcome to the contact book! \n These are all available functions: \n 1. Create a contact \n 2. View a contact \n 3. View all contacts \n 4. Delete a contact")

while True:
    display_menu()
    Action = input("Enter the number of the function you want to use: ")
    if Action == '1':
        create_contact(contacts)
        while True:
            Create_More = input('Do you want to create more contacts? (yes/no): ').lower()
            if Create_More == 'yes':
                create_contact(contacts)
            else:
                print("Thank you for using the contact book")
                break
    elif Action == '2':
        view_contact(contacts)
    elif Action == '3':
        view_all_contacts(contacts)
    elif Action == '4':
        delete_contact(contacts)
    else:
        print("Invalid input! Please try again.")
