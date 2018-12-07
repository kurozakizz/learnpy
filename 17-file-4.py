with open('config/chat_history') as chat_file:
    for line in chat_file:
        print(line)

print('-' * 10)
with open('config/chat_history') as chat_file:
    for line in chat_file:
        print(line.rstrip())