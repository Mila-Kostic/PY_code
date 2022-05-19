from random import randint

tajni_broj = randint(1,100)
brojac_pokusaja = 0
pokusaj = 0

while pokusaj != tajni_broj and brojac_pokusaja <=4:  #uslov while petelje
    pokusaj = eval(input(' Unesite vas pokusaj (1-100): '))
    brojac_pokusaja = brojac_pokusaja + 1
    #if naredba za ispitivanje da li je pokusaj koji korisnik unosi manji ili veci
    if pokusaj < tajni_broj:
        print('VECI.', 5-brojac_pokusaja, 'preostalih pokusaja.\n')
    elif pokusaj > tajni_broj:
        print('MANJI.', 5-brojac_pokusaja, 'preostalih pokusaja.\n')
    else:
        print('Pogodili ste!')
# obavestenje korisniku kroz naredbu u dodatne dve linije koda o ishodu igre

brojac_pokusaja==5 and pokusaj != tajni_broj
print('Izgubili ste. Tacan odgovor je', tajni_broj)
