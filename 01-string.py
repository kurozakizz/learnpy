fruit = 'AppLe'
fruit_len = len(fruit)
print(fruit[1])
print(fruit_len)
print(fruit.upper())
print(fruit.lower())

print('I ' + 'Love ' + 'Py')
print('-' * 10)
print(fruit + ' ' + str(fruit_len))

print('I {} Python.'.format('love'))
print('{} {} {}'.format('I', 'love', 'Python.'))
print('I {0} {1}. {1} {0}s me.'.format('love', 'Python'))

print('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8}'.format('Apple', '3'))
print('{0:8} | {1:8}'.format('Orange', '10'))

print('{0:^8} | {1:^8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:>8}'.format('Apple', '3'))
print('{0:8} | {1:>8}'.format('Orange', '10'))

print('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8.2f}'.format('Apple', 2.3333))
print('{0:8} | {1:8.2f}'.format('Orange', 10))