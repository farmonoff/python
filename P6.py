n = int(input('Faylning hajmini kiriting: '))
kb = int(n / 1024)
bayt = int(n - (kb * 1024))
print('%d kb %d bayt' % (kb, bayt))