import json

try:
    with open('Computer Science 2\Chapter 10\contacts.json', 'r') as file:
        database = json.load(file)
except FileNotFoundError:
    database = {}

print('1. Add a new name')
print('2. Change a name')
print('3. Delete a name')
print('4. Look up a name')
print('5. Quit the program')

choice = int(input('Enter your choice: '))
while choice != 5:
    if choice == 1:
        # Add a new name
        name = input('Enter a name: ')
        if name not in database:
            phone = input('Enter a phone number: ')
            database[name] = phone
            with open('Computer Science 2\Chapter 10\contacts.json', 'w') as fp:
                json.dump(database, fp)
        else:
            print('That name already exists.')

    elif choice == 2:
        # Change an existing name
        name = input('Enter a name: ')
        if name in database:
            phone = input('Enter the new phone number: ')
            database[name] = phone
            with open('Computer Science 2\Chapter 10\contacts.json', 'w') as fp:
                json.dump(database, fp)
        else:
            print('That name is not found.')

    elif choice == 3:
        # Delete an existing name
        name = input('Enter a name: ')
        if name in database:
            del database[name]
            with open('Computer Science 2\Chapter 10\contacts.json', 'w') as fp:
                json.dump(database, fp)
                
        else:
            print('That name is not found.')

    elif choice == 4:
        # Look up a name
        name = input('Enter a name: ')
        if name in database:
            print('The phone number is', database[name])
        else:
            print('That name is not found.')

    else:
        print('The valid choices are 1 through 5.')
        print('Please run the program again.')

    choice = int(input('Enter your choice: '))