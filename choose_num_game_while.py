from random import randint

tajni_broj = randint(1,100)
brojac_pokusaja = 0
pokusaj = 0

#uslov petlje#
while pokusaj != tajni_broj and brojac_pokusaja <= 4:
    pokusaj = eval(input('Unesite vas pokusaj (1-100): '))
    brojac_pokusaja = brojac_pokusaja + 1
    # if naredba za ispitivanje da li je pokusaj manji ili veci manji
# while pokusaj != tajni_broj and brojac_pokusaja <= 4:
    if pokusaj < tajni_broj:
        print('VECI.', 5-brojac_pokusaja, 'preostalih pokusaja.\n')
    elif pokusaj > tajni_broj:
        print('MANJI.', 5-brojac_pokusaja, 'preostalih pokusaja.\n')    
    else:
        print('Pogodili ste!')
                    
if brojac_pokusaja==5 and pokusaj != tajni_broj:
    print('Izgubili ste. Tacan odgovor je', tajni_broj)

