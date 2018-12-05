animals = ['man', 'bear', 'pig']
bear_index = animals.index('bear')
print('bear index {}'.format(bear_index))

find = 'cat'
try:
    find_index = animals.index(find)
except:
    find_index = 'Not found ' + find + '.'
print(find_index)