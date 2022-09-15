cadena="Geringoso"
vocales="aeiou"
capadepenapa=""

for c in cadena:
    if c in vocales:
        capadepenapa+=c+"p"+c
    else:
        capadepenapa+=c

print(capadepenapa)

#salida
#Geperipingoposopo
