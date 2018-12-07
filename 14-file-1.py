config_file = open('config/connection')
connection = config_file.read()
print(connection)

print('File closed? {}'.format(config_file.closed))

if not config_file.closed:
    config_file.close()
print('File closed? {}'.format(config_file.closed))