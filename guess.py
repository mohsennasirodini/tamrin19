from random import randint

n = randint(1, 100)
c = 0

while c < 7:
    c += 1
    a = int(input('? '))
    if n == a:
        print('You won!')
        exit()
    elif n > a:
        print('Greater')
    elif n < a:
        print('Smaller')

print('You lost!')