temp = eval(input('Unesite temperaturu u Celzijusima: '))
while temp<-273.15:
    temp = eval(input('Nemoguce. Unesite ispravnu temperaturu: '))
print('U Faranhajtima to je', 9/5*temp+32)