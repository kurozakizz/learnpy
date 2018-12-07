config = open('config/connection')
print('Current position: {}'.format(config.tell()))
print(config.read())

print('Current position: {}'.format(config.tell()))
print(config.read())

config.seek(0)
print('Current position: {}'.format(config.tell()))
print(config.read())

config.seek(0)
print('Current position: {}'.format(config.tell()))
print(config.read(5))
print(config.read())