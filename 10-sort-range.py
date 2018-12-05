animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']
sorted_animals = sorted(animals)

print('Animal list: {}'.format(animals))
print('Sorted animal list: {}'.format(sorted_animals))

animals.sort()
print('Animals after sort: {}'.format(animals))
print(len(animals))

animals.append('cat')
print(len(animals))

print('-' * 10)
for number in range(3):
    print(number)

print('-' * 10)
for number in range(1, 3):
    print(number)

print('-' * 10)
for number in range(1, 10, 2):
    print(number)

print('-' * 10)
for i in range(0, len(animals), 2):
    print(animals[i])
