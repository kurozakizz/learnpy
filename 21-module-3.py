import sys

file_name = 'config/connectionx'

try:
    with open(file_name) as connection_file:
        print(connection_file.read())
except:
    print('File {} cannot be opened'.format(file_name))
    sys.exit()