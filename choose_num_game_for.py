from random import randint

tajni_broj = randint(1,100)

for brojac_pokusaja in range (5):
    pokusaj = eval(input('Enter your guess (1 - 100): '))
    if pokusaj < tajni_broj:
        print('VECI.', 5-brojac_pokusaja, 'preostalih pokusaja.\n')
    elif pokusaj > tajni_broj:
        print('MANJI.', 5-brojac_pokusaja, 'preostalih pokusaja.\n')
    else:
        print('Pogodili ste!')
        break
else: 
    print('Izgubili ste. Tacan odgovor je', tajni broj)
