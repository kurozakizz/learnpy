with open('config/connection') as connection_file:
    print(connection_file.mode)

with open('config/file1', 'w') as the_file:
    the_file.write('first\n')
    the_file.write('second')

with open('config/file1') as the_file:
    print(the_file.read())