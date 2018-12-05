def say_hi(first = 'Jane', last = 'Doe'):
    """Say hello to there name."""
    print('Hi! {} {}'.format(first, last))

say_hi()
say_hi(first='Nuttawoot', last='Singhathom')

def odd_or_even(num):
    """Determine number is odd or even"""
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(odd_or_even(2))
print(odd_or_even(1))

def is_even(num):
    """Is number even"""
    return num % 2 == 0

print(is_even(1))
print(is_even(2))