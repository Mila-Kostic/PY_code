for i in range (10):
    num = eval(input('Unesite broj: '))
    if num < 0:
        print('program prekinut ranije')
        break
else: 
    print ('Korisnik je uneo svih deset brojeva')