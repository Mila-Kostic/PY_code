broj_tacnih = 0

#pitanje 1
print('Koji je glavni grad Francuske?', end = ' ')
odgovor = input()
if odgovor.lower()=='pariz':
    print('Tacno!')
    broj_tacnih+=1
else: 
    print('Pogresno. Tacan odgovor je Pariz.')
print('Imate', broj_tacnih, 'od 1 tacnih odgovora.')


#pitanje 2
print('Sa koliko drzava se granici Madjarska?', end=' ')
odgovor = input()
if odgovor =='7':
    print('Tacno!')
    broj_tacnih+=1
else:
    print('pogresno. Tacan odgovor je 7.')
print('Imate', broj_tacnih, 'od 2 tacnih odgovora.')