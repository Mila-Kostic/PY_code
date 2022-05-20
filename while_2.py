temp = eval(input('Unesite temperaturu u Celzijusima: ')) 
if temp < -273.15:
    print('Nemoguca temperatura.')
else:
    print('U Farenhajtima to je', 9/5*temp+32)