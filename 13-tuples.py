days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
monday = days[0]
print(monday)
for d in days:
    print(d)

# list to tuple
weekend_tuple = ('Saturday', 'Sunday')
weekend_list = list(weekend_tuple)
print('weekend_tuple is {}'.format(type(weekend_tuple)))
print('weekend_list is {}'.format(type(weekend_list)))

# tuple to list
animal_list = ['man', 'bear', 'pig']
animal_tuple= tuple(animal_list)
print('animal_list is {}'.format(type(animal_list)))
print('animal_tuple is {}'.format(type(animal_tuple)))

weekend_days = ('Saturday', 'Sunday')
(sat, sun) = weekend_days
print(sat)
print(sun)

contact_info = ['555-0123', 'jason@example.com']
(phone, email) = contact_info
print(phone)
print(email)

def high_and_low(numbers):
    """Returns highest and lower number."""
    high = max(numbers)
    low = min(numbers)
    return (high, low)

lottery_numbers = [16, 4, 42, 15, 23, 8]
(highest, lowest) = high_and_low(lottery_numbers)
print('Highest number is {}'.format(highest))
print('Lowest number is {}'.format(lowest))

contacts = [('Jason', '555-0123'), ('Carl', '555-0987')]
for (name, phone) in contacts:
    print('{}\'s number is {}'.format(name, phone))