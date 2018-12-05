contacts = {'Jason': '555-0123', 'Carl': '555-0787'}
jason_phone = contacts['Jason']
carl_phone = contacts['Carl']

print('Dial {} to call Jason'.format(jason_phone))
print('Dial {} to call Carl'.format(carl_phone))

contacts['Tony'] = '555-0570'
print(contacts)
print(len(contacts))

del contacts['Jason']
print(contacts)

new_contacts = {
    'Jason': ['555-0123', '555-0000'],
    'Carl': '555-0787'
}
print(new_contacts['Jason'])
print(new_contacts['Jason'][1])
print(new_contacts['Carl'])

print('Json Contacts')
for number in new_contacts['Jason']:
    print(number)

if 'Jason' in new_contacts.keys():
    print('Jason phone number is {}'.format(new_contacts['Jason'][0]))

if 'Nut' in new_contacts.keys():
    print('Nut phone number is {}'.format(new_contacts['Nut'][0]))

print('555-0787' in new_contacts.values())
