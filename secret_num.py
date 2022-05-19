from random import randint
secret_num = randint(1,10)
pokusaj = 0
while pokusaj != secret_num:
    pokusaj = eval(input('Pogodi tajni broj:'))
print('Konacno ste pogodili!')
