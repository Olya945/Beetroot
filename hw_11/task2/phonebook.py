import json
import sys

# Функція виводу меню
def show_menu():
    print('\n' + '=' * 50)
    print('Phonebook')
    print('=' * 50)
    print('1. Add new entry')
    print('2. Search by first name')
    print('3. Search by last name')
    print('4. Search by full name')
    print('5. Search by telephone number')
    print('6. Search by city or state')
    print('7. Delete a record')
    print('8. Update a record')
    print('9. Exit')
    print('=' * 50)

# Функція додавання нового контакту
def add_contact(contacts):
    print('\n' + '=' * 50)
    print('Add new contact')
    print('=' * 50)

    # Введення номеру телефону
    while True:
        phone_number = input('\nTo add a new contact, enter the phone number in the format +380XXXXXXXXX: ').strip()
        
        # Перевірка коректності введеного номеру телефону
        is_valid = (
            len(phone_number) == 13 and
            phone_number.startswith('+380') and
            phone_number[1:].isdigit()
        )

        if not is_valid:
            print('\nInvalid phone number format! Try again.')
            #input('\nPress Enter to continue...')
            continue
        
        if phone_number in contacts:
            print('\nContact with this phnone number already exists!')
            continue
        break
        
    print('\nEnter contact information: ')

    # Введення імені, прізвища, міста та регіону
    while True:
        first_name = input('First name: ').strip()
        if not first_name:
            print('\nThe name was not entered! Try again.')
            #input('\nPress Enter to continue...')
            continue
        break
    
    while True:     
        last_name = input('Last name: ').strip()
        if not last_name:
            print('\nThe last name was not entered! Try again.')
            #input('\nPress Enter to continue...')
            continue
        break  
    
    while True:
        city = input('City: ').strip()
        if not city:
            print('\nThe city was not entered! Try again.')
            #input('\nPress Enter to continue...')
            continue
        break

    while True:
        state = input('State: ').strip()
        if not state:
            print('\nThe state was not entered! Try again.')
            #input('\nPress Enter to continue...')
            continue
        break
    
    contacts[phone_number] = {
        'first_name': first_name,
        'last_name': last_name,
        'city': city,
        'state': state
        }

    print('=' * 50)                   
    print(f'\nYou added a new contact!')
    print(f'Phone number: {phone_number}')
    print(f'First name: {first_name}')
    print(f'Last name: {last_name}')
    print(f'City: {city}')
    print(f'State: {state}')
    input('\nPress Enter to continue...')

# Функція пошуку за ім'ям
def search_by_first_name(contacts):
    print('\n' + '=' * 50)
    print('Search by first name')
    print('=' * 50)

    first_name = input('\nEnter the first name to search: ').strip()

    if not first_name:
        print('\nThe name was not entered! Try again.')
        #input('\nPress Enter to continue...')
        return
    
    found = []
    for phone, info in contacts.items():
        if info['first_name'].lower() == first_name.lower():
            found.append((phone, info))
        
    if found:
        print(f'\nFound {len(found)} contact(s):')
        print('-' * 50)
        for phone, info in found:
            print(f'\nPhone number: {phone}')
            print(f'First name: {info["first_name"]} {info["last_name"]}')
            print(f'City: {info["city"]}')
            print(f'State: {info["state"]}')
            print('-' * 50)
    
    else:
        print(f'\nNo contacts found with that "{first_name}"')
    
    input('\nPress Enter to continue...')

# Функція пошуку за прізвищем
def search_by_last_name(contacts):
    print('\n' + '=' * 50)
    print('Search by last name')
    print('=' * 50)

    last_name = input('Enter the last name to search: ').strip()
    if not last_name:
        print('\nThe last name was not entered! Try again.')
        #input('\nPress Enter to continue...')
        return
    
    found = []
    for phone, info in contacts.items():
        if info['last_name'].lower() == last_name.lower():
            found.append((phone, info))
    
    if found:
        print(f'\nFound {len(found)} contact(s):')
        print('-' * 50)
        for phone, info in found:
            print(f'\nPhone number: {phone}')
            print(f'First name: {info["first_name"]} {info["last_name"]}')
            print(f'City: {info["city"]}')
            print(f'State: {info["state"]}')
            print('-' * 50)
    else:
        print(f'\nNo contacts found with that "{last_name}"')
    
    input('\nPress Enter to continue...')

# Функція пошуку за повним ім'ям
def search_by_full_name(contacts):
    print('\n' + '=' *50)
    print('Search by full name')
    print('=' * 50)

    full_name = input('Enter the full name to search (First Last): ').strip()
    if not full_name:
        print('\nThe full name was not entered! Try again.')
        #input('\nPress Enter to continue...')
        return
    
    found = []
    for phone, info in contacts.items():
        if f"{info['first_name']} {info['last_name']}".lower() == full_name.lower():
            found.append((phone, info))
    
    if found:
        print(f'\nFound {len(found)} contact(s):')
        print('-' * 50)
        for phone, info in found:
            print(f'\nPhone number: {phone}')
            print(f'First name: {info["first_name"]} {info["last_name"]}')
            print(f'City: {info["city"]}')
            print(f'State: {info["state"]}')
            print('-' * 50)
    else:
        print(f'\nNo contacts found with that "{full_name}"')

    input('\nPress Enter to continue...')

# Функція пошуку за номером телефону
def search_by_phone_number(contacts):
    print('\n' + '=' * 50)
    print('Search by phone number')
    print('=' * 50)

    phone_number = input('Enter the phone number to search (format +380XXXXXXXXX): ').strip()
    if not phone_number:
        print('\nThe phone number was not entered! Try again.')
        #input('\nPress Enter to continue...')
        return
    
    if phone_number in contacts:
        info = contacts[phone_number]
        print('\nContact found:')
        print('-' * 50)
        print(f'\nPhone number: {phone_number}')
        print(f'First name: {info["first_name"]} {info["last_name"]}')
        print(f'City: {info["city"]}')
        print(f'State: {info["state"]}')
        print('-' * 50)
   
    else:
        print(f'\nNo contacts found with that "{phone_number}"')

    input('\nPress Enter to continue...')

# Функція пошуку за містом або регіоном
def search_by_city_or_state(contacts):
    print('\n' + '=' * 50)
    print('Search by city or state')
    print('=' * 50)

    location = input('Enter the city or state to search: ').strip()
    if not location:
        print('\nThe city or state was not entered! Try again.')
        #input('\nPress Enter to continue...')
        return
    
    found = []
    for phone, info in contacts.items():
        if info['city'].lower() == location.lower() or info['state'].lower() == location.lower():
            found.append((phone, info))

    if found:
        print(f'\nFound {len(found)} contact(s):')
        print('-' * 50)
        for phone, info in found:
            print(f'\nPhone number: {phone}')
            print(f'First name: {info["first_name"]} {info["last_name"]}')
            print(f'City: {info["city"]}')
            print(f'State: {info["state"]}')
            print('-' * 50)
    else:
        print(f'\nNo contacts found in "{location}"')
   
    input('\nPress Enter to continue...')

# Функція видалення контакту
def delete_contact(contacts):
    print('\n' + '=' * 50)
    print('Delete a record')
    print('=' * 50)

    phone_number = input('Enter the phone number of the contact to delete (format +380XXXXXXXXX): ').strip()
    if not phone_number:
        print('\nThe phone number was not entered! Try again.')
        #input('\nPress Enter to continue...')
        return
    
    if phone_number in contacts:
        info = contacts[phone_number]
        print('\nContact found:')
        print('-' * 50)
        print(f'\nPhone number: {phone_number}')
        print(f'First name: {info["first_name"]} {info["last_name"]}')
        print(f'City: {info["city"]}')
        print(f'State: {info["state"]}')
        print('-' * 50)

        confirmation = input('\nAre you sure you want to delete this contact? (yes/no): ').strip().lower()
        if confirmation == 'yes':
            del contacts[phone_number]
            print('\nContact has been deleted')
        
        elif confirmation == 'no':
            print('\nDeletion cancelled')
        
        else:
            print('\nInvalid input! Deletion cancelled')
    else:
        print(f'\nNo contacts found with that "{phone_number}"')
    
    input('\nPress Enter to continue...')

# Функція оновлення контакту
def update_contact(contacts):
    print('\n' + '=' * 50)
    print('Update a record')
    print('=' * 50)

    phone_number = input('\nEnter the phone number to update (+380XXXXXXXXX): ').strip()
   
    if not phone_number:
        print('\nThe phone number was not entered! Try again.')
        return

    is_valid = (
        len(phone_number) == 13 and
        phone_number.startswith('+380') and
        phone_number[1:].isdigit()
    )

    if not is_valid:
        print('\nInvalid phone number format! Try again.')
        return
    
    if phone_number in contacts:
        info = contacts[phone_number]

        print('\nContact found:')
        print('-' * 50)
        print(f'\nPhone number: {phone_number}')
        print(f'First name: {info["first_name"]} {info["last_name"]}')
        print(f'City: {info["city"]}')
        print(f'State: {info["state"]}')
        print('-' * 50)

        new_phone_number = input('\nEnter new phone number or press Enter to keep the current number: ').strip()
        
        if new_phone_number:
            is_valid_new = (
                len(new_phone_number) == 13 and
                new_phone_number.startswith('+380') and
                new_phone_number[1:].isdigit()
            )

            if not is_valid_new:
                print('\nInvalid phone number format! Phone number remains unchanged.')
            
            elif new_phone_number in contacts:
                print('\nContact with this phone number already exists! Phone number remains unchanged.')
        
            else:
                del contacts[phone_number]
                contacts[new_phone_number] = info
                phone_number = new_phone_number
                print(f'\nPhone number changed to: {new_phone_number}')
                print('-' * 50)
        else:
            print('\nPhone number remains unchanged.')
            print('-' * 50) 
        
    
        new_first_name = input('\nEnter new name or press Enter to keep the current number: ').strip()
        if new_first_name:
            info['first_name'] = new_first_name
            print(f'\nName changed to: {new_first_name}')
            print('-' * 50)
        
        else:
            print('\nName remains unchanged.')
            print('-' * 50)
        
        new_last_name = input('\nEnter new last name or press Enter to keep the current last name: ').strip()
        if new_last_name:
            info['last_name'] = new_last_name
            print(f'\nLast name changed to: {new_last_name}')
            print('-' * 50)
        else:
            print('\nLast name remains unchanged.')
            print('-' * 50)


        new_city = input('\nEnter new city or press Enter to keep the current city: ').strip()
        if new_city:
            info['city'] = new_city
            print(f'\nCity changed to: {new_city}')
            print('-' * 50)
        else:   
            print('\nCity remains unchanged.')
            print('-' * 50)
        
        new_state = input('\nEnter new state or press Enter to keep the current state: ').strip()
        if new_state:
            info['state'] = new_state
            print(f'\nState changed to: {new_state}')

        else:   
            print('\nState remains unchanged.')
            print('-' * 50)
        

        print('\nYour data has been saved!')
        print('-' * 50)
        print('Contact updated successfully!')
        print('=' * 50)
        print(f'\nUpdated contact details:')
        print(f'Phone number: {phone_number}')
        print(f'First name: {info["first_name"]} {info["last_name"]}')
        print(f'City: {info["city"]}')
        print(f'State: {info["state"]}')
        print('=' * 50)
    
    else:
        print(f'\nNo contacts found with that "{phone_number}"')

    input('\nPress Enter to continue...')     


# Перевіряємо аргументи
if len(sys.argv) < 2:
    print('Error: Enter the file\'s name')

else:
    file_name = sys.argv[1]

    # Відкриваємо файл та виводимо інформацію про контакти
    with open(file_name, 'r', encoding='utf-8') as file:
        contacts = json.load(file)

    print(f'Loaded {len(contacts)} contacts from {file_name}')

    # Виводимо меню
    while True:
        show_menu()
        choice = input('\nChoose option from 1 to 9: \n')

        if choice == '1':
            add_contact(contacts)
            #print('\nDEBAG: add_contact завершено')
        
        elif choice == '2':
            search_by_first_name(contacts)
            #print('Search by first name')
        
        elif choice == '3':
            search_by_last_name(contacts)
            
        
        elif choice == '4':
            search_by_full_name(contacts)
           
        
        elif choice == '5':
            search_by_phone_number(contacts)
            
        
        elif choice == '6':
            search_by_city_or_state(contacts)
            
        
        elif choice == '7':
            delete_contact(contacts)
           
        
        elif choice == '8':
            update_contact(contacts)
           
        elif choice == '9':
            print('\nGoodbye')

            # Збереження файлу перед виходом
            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump(contacts, file, indent=2, ensure_ascii=False)
            print(f'Information saved to {file_name}')
            break

        else:
            print('\nInvalid choice! Try again.')
            input('\nPress Enter to continue...')


