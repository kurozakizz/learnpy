colors = ['red', 'green', 'blue']
print('{} {} {}'.format(colors[0], colors[1], colors[2]))
print('{} {} {}'.format(colors[-1], colors[-2], colors[-3]))

colors[2] = 'black'
print(colors[2])

more_colors = ['yellow', 'pink']
colors.extend(more_colors)
print(colors)

colors.insert(1, 'brown')
print(colors)
print(len(colors))