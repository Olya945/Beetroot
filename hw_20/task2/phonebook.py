import os
import json


# general settings
DEFAULT_DATABASE_NAME = "phonebook.json"
__DEVELOPMENT_MODE__ = os.environ.get('DEVELOPMENT_MODE', False)


# common functions
def load_db(db_name):
    try:
        with open(db_name) as file:
            db = json.load(file)
    except FileNotFoundError:
        db = {'contacts': []}
    except json.JSONDecodeError:
        db = {'contacts': []}
    return db


def save_db(db_name, db):
    with open(db_name, 'w') as file:
        json.dump(db, file)


# add contact
def add_contact(db_name):
    if __DEVELOPMENT_MODE__:
        phone_number = '123'
        name = 'User1'
        city = 'City1'
    else:
        phone_number = input('Enter number (only digits): ')
        name = input('Enter name: ')
        city = input('Enter city: ')

    clean_number = phone_number.strip()
    datum = {'number': clean_number, 'name': name, 'city': city}

    db = load_db(db_name)
    db['contacts'].append(datum)
    save_db(db_name, db)
    print("Contact added successfully.")


# contact update
def validate_phone(phone):
    if not phone:
        return (False, 'You did not enter a phone number. Try again.')
    if not phone.isdigit():
        return (False, 'The phone number must contain only digits. Try again.')
    if len(phone) != 10:
        return (False, 'The phone number must contain 10 digits. Try again.')
    return (True, 'Valid phone number.')


def update_contact(db_name):
    db = load_db(db_name)

    updating = True
    while updating:

        phone_valid = False
        while not phone_valid:
            phone_number = input("\nEnter the phone number to update or 'q' to quit: ").strip()
            if phone_number.lower() == 'q':
                print("\nUpdate canceled.")
                return
            
            is_valid, message = validate_phone(phone_number)
            if is_valid:
                phone_valid = True
            
            else:
                print(message)

        for entry in db["contacts"]:
            if entry["number"] == phone_number:
                contact_info = {
                    'Phone': entry['number'],
                    'Name': entry['name'],
                    'City': entry['city']
                }
                print("\nYou are updating the following contact:")
                for key, value in contact_info.items():
                    print(f"{key}: {value}")

                new_number = input("\nEnter a new phone number or press Enter to keep the same: ").strip()
                if new_number:
                    is_valid, message = validate_phone(new_number)
                    if not is_valid:
                        print(message)
                        return
        
                    for c in db["contacts"]:
                        if c["number"] == new_number and c is not entry:
                            print("\nA contact with this number already exists. Update canceled.")
                            return
                    entry["number"] = new_number
                    print(f"\nPhone number changed to: {new_number}")
                else:
                    print("\nPhone number was not changed.")

                new_name = input("\nEnter a new name or press Enter to keep the same: ").strip()
                if new_name:
                    entry["name"] = new_name
                    print(f"\nName changed to: {new_name}")
                else:
                    print("\nName was not changed.")

                new_city = input("\nEnter a new city or press Enter to keep the same: ").strip()
                if new_city:
                    entry["city"] = new_city
                    print(f"\nCity changed to: {new_city}")
                else:
                    print("\nCity was not changed.")

                save_db(db_name, db)
                print("\nYour changes have been saved!")
                return
        else:
            print("\nNo contact found with that phone number.")
            try_again = input("Do you want to try again? (y/n): ").strip().lower()
            if try_again != 'y':
                print("\nUpdate canceled.")
                return


# list all contacts
def list_contact(db_name):
    db = load_db(db_name)
    contacts = db.get('contacts', [])
    if not contacts:
        print("List of contacts is empty.")
        return
    
    print("\nList of contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact.get('name', '')} | "
              f"Phone: {contact.get('number', '')} | "
              f"City: {contact.get('city', '')}")


# delete contact
def delete_contact(db_name):
    if __DEVELOPMENT_MODE__:
        search_key = " "
    else:
        search_key = input('Enter the number or name of the contact you want to delete: ').strip()

    db = load_db(db_name)
    contacts = db.get('contacts', [])
    updated_contacts = [
        c for c in contacts
        if c['number'] != search_key and c['name'].lower() != search_key.lower()
    ]

    if len(updated_contacts) == len(contacts):
        print("Contact not found.")
        return

    db['contacts'] = updated_contacts
    save_db(db_name, db)
    print(f"Contact '{search_key}' successfully deleted.")


# contact search
def find_contact(db_name):
    db = load_db(db_name)
    search = input('Enter a name OR phone number to search for: ').strip()
    found = False

    for contact in db['contacts']:
        if contact['name'] == search or contact['number'] == search:
            print(f"""Contact found:
Name: {contact['name']}
Phone number: {contact['number']}
City: {contact['city']}""")
            found = True

    if not found:
        print('No contact found.')


# main menu
def main():
    db_name = DEFAULT_DATABASE_NAME
    while True:
        print("\nPHONEBOOK MENU")
        print("1 - Add contact")
        print("2 - Update contact")
        print("3 - List all contacts")
        print("4 - Delete contact")
        print("5 - Find contact")
        print("0 - Exit")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_contact(db_name)
        elif choice == '2':
            update_contact(db_name)
        elif choice == '3':
            list_contact(db_name)
        elif choice == '4':
            delete_contact(db_name)
        elif choice == '5':
            find_contact(db_name)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Unknown choice, try again.")


if __name__ == "__main__":
    main()


