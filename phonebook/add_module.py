import os
import json

# Change that if you don't want to enter data manually
__DEVELOPMENT_MODE__ = os.environ.get('DEVELOPMENT_MODE', False)


def add_contact(db_name):
    """Get user input, and create a contact if absent"""
    if __DEVELOPMENT_MODE__:
        phone_number = "123"
        name = "User1"
        city = "City1"
    else:
        phone_number = input('enter number, only digits ')
        name = input('enter name ')
        city = input('enter city ')

    # Assume only numbers are in phone_number
    clean_number = phone_number.strip()

    # Construct a line to be written into database
    datum = {'number': clean_number, 'name': name, 'city': city}

    # open database and parse it into json
    db = json.load(open(db_name))

    # append item to the contacts list
    db['contacts'].append(datum)

    # write `db` dictionary to the json database
    json.dump(db, open(db_name, 'w'))



if __name__ == '__main__':
    from phonebook import DEFAULT_DATABASE_NAME
    add_contact(DEFAULT_DATABASE_NAME)