num = eval(input('Unesite broj: '))
for i in range (2, num):
    if num % i == 0:
        print('Nije prost')
        break
else: print('Prost')