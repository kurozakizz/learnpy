contacts = {
    'Jason': '555-0123',
    'Carl': '555-0787'
}

for person, phone in contacts.items():
    print('The number for {0} is {1}'.format(person, phone))

contacts = {
    'Jason': {
        'phone': '555-0123',
        'email': 'jason@example.com'
    },
    'Carl': {
        'phone': '555-0987',
        'email': 'carl@example.com'
    }
}

for c in contacts:
    print('{}\'s contact info:'.format(c))
    print(contacts[c]['phone'])
    print(contacts[c]['email'])
