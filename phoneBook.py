contacts = {}

def new(key, value):
    contacts[key] = value
    
while True:
    user_input = input('command: ')

    if user_input == 'exit':
        break
    
    elif user_input == 'add':
        useri_name = input('Enter name of contact: ').lower()
        useri_numb = input('Enter phone number of contact: ')
        if useri_name in contacts:
            print('Contact already exists. Do you want to overwrite it?')
        else:
            contacts[useri_name] = useri_numb
            print('Contact added successfully')
        print()

    elif user_input == 'view':
        ...
        print() 
        #better way to check
        if not contacts:
            print('Contacts is empty')
        else:
            print('Contact List')
            for key, value in contacts.items():
                print('{0} | {1}' .format(key.capitalize(), value))

    elif user_input.startswith('get '):
        search = user_input[4:].lower()
        #result = contacts.get(search, 'Contact not found')
        if search in contacts:
            result = contacts[search]
            print(f'{search.capitalize()} | {result}')
        else:
            print('Contact not found')
        print()
