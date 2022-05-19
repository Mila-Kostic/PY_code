temp = 0
while temp != -1000:
    temp = eval(input('Unesite temperaturu (-1000 za kraj): '))
    if temp!=-1000:
        print('U Faranhajtima to je ', 9/5*temp+32)
    else:
        print('Kraj!')
