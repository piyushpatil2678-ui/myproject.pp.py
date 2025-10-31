contacts = {}

while True:
    print("\nContact Book App")
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. Search contact')
    print('6. Count contact')
    print('7. Exit')

    choice = input('Enter your choice = ')

    if choice == '1':
        name = input('Enter your name = ')
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            age = input('Enter age = ')
            email = input('Enter email = ')
            mobile = input('Enter mobile number = ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print("Contact added successfully!")

    elif choice == '2':
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Age: {details['age']}, Email: {details['email']}, Mobile: {details['mobile']}")

    elif choice == '3':
        name = input('Enter name to update = ')
        if name in contacts:
            age = input('Enter new age = ')
            email = input('Enter new email = ')
            mobile = input('Enter new mobile number = ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print("Contact Updated!")
        else:
            print("Contact not found!")

    elif choice == '4':
        name = input('Enter name to delete = ')
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif choice == '5':
        name = input('Enter name to search = ')
        if name in contacts:
            print(f"Name: {name}")
            print(f"Age: {contacts[name]['age']}")
            print(f"Email: {contacts[name]['email']}")
            print(f"Mobile: {contacts[name]['mobile']}")
        else:
            print("Contact not found!")

    elif choice == '6':
        print(f"Total contacts = {len(contacts)}")

    elif choice == '7':
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
