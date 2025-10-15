import json

def validate_phone(phone):

    if not phone:
        print("\nYou did not enter a phone number. Try again.")
        return False

    if not phone.isdigit():
        print("\nThe phone number must contain only digits. Try again.")
        return False

    if len(phone) != 10:
        print("\nThe phone number must contain 10 digits. Try again.")
        return False

    return True

def update_contact(db_name):
    with open(db_name, "r", encoding="utf-8") as f:
        db = json.load(f)


    while True:
        while True:
            phone_number = input("\nEnter the phone number to update or 'q' to quit: ").strip()
            if phone_number.lower() == 'q':
                print("\nUpdate canceled.")
                return
            
            if validate_phone(phone_number):
                break


        for entry in db["contacts"]:
            if entry["number"] == phone_number:
                print("\nYou are updating the following contact:")
                print(f"\nPhone: {entry['number']}")
                print(f"Name: {entry['name']}")
                print(f"City: {entry['city']}")

                new_number = input("\nEnter a new phone number or press Enter to keep the same: ").strip()

                if new_number:
                    if not validate_phone(new_number):
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
                
                print('-' * 40)

                with open(db_name, "w", encoding="utf-8") as f:
                    json.dump(db, f, ensure_ascii=False, indent=2)

                print("\nYour changes have been saved!")
                return
        else:
            print("\nNo contact found with that phone number. Please try again.")
            try_again = input("Do you want to try again? (y/n): ").strip().lower()
            if try_again != 'y':
                print("\nUpdate canceled.")
                return 

if __name__ == '__main__':
    from phonebook import DEFAULT_DATABASE_NAME
    update_contact(DEFAULT_DATABASE_NAME)