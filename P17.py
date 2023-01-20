n = int(input('Qator: '))
m = int(input('Katak: '))

if n % 2:
    if m % 2:
        print('Oq') 
    elif not m % 2:
        print('Qora')
elif not n % 2:
    if m % 2:
        print('Qora')
    elif not m % 2:
        print('Oq')    
