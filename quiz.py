pitanja = ['Koji je glavni grad Francuske?', 
            'Sa koliko drzava se granici Madjarska?']
odgovori = ['Pariz', '7']

broj_tacnih = 0

for i in range(len(pitanja)):
    odgovor = input(pitanja[i])
    if odgovor.lower()==odgovori[i].lower():
        print('Tacno')
        broj_tacnih=broj_tacnih+1
    else: 
        print('Pogresno. Tacan odgovor je ', odgovori[i]) 
    print('Imate', broj_tacnih, 'od', i, 'tacnih odgovora.')   