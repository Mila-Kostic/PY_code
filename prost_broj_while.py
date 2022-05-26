i=2
num = eval(input('Unesite broj: '))
while i < num and num % i != 0:
    i = i+1
if i == num:
    print('Prost')
else:
     print('Nije prost')