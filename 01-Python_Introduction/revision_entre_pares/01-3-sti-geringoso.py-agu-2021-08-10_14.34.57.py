cadena = 'Geringoso'
capadepenapa = ''
# en principio, por mis conocimientos
#llegue a este programa que no es correcto

for c in cadena:
	if ('a' in c):
		capadepenapa = (cadena).replace('a', 'apa') 
	if ('e' in c):
		capadepenapa = (cadena).replace('e', 'epe') 
	if ('i' in c):
		capadepenapa = (cadena).replace('i', 'ipi') 
	if ('o' in c):
		capadepenapa = (cadena).replace('o', 'opo') 
	if ('u' in c):
		capadepenapa = (cadena).replace('u', 'upu')

print (capadepenapa)

#volvi a ver las clases y en un video usan if (c in 'aeiou')
#lo cual no sabia que era posible
#tambien consulte con compañeres y llegue a estos resultados

for c in cadena:
	if (c in 'aeiou'):
		capadepenapa = capadepenapa + c + 'p' + c 
	else: 
		capadepenapa = capadepenapa + c

print (capadepenapa)

for a in cadena:
	capadepenapa += a
	if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
		capadepenapa += 'p'+a

print(capadepenapa)

