print('start reading file...')
with open('config/connection') as config_file:
    print('file closed? {}'.format(config_file.closed))
    print(config_file.read())

print('finished reading file')
print('file closed? {}'.format(config_file.closed))
