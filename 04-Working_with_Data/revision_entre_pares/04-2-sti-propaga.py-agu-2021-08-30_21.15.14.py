
# 4.6. Imaginate una fila con varios fósforos uno al lado del otro. Los 
# fósforos pueden estar en tres estados: nuevos, prendidos fuego o ya gastados
# (carbonizados). Representaremos esta situación con una lista L con un 
# elemento por fósforo, que en cada posición tiene un 0 (nuevo), un 
# 1 (encendido) o un -1 (carbonizado). El fuego se propaga inmediatamente de
# un fósforo encendido a cualquier fósforo nuevo que tenga a su lado. Los 
# fósforos carbonizados no se encienden nuevamente.

# Escribí una función llamada propagar que reciba un vector con 0's, 
# 1's y -1's y devuelva un vector en el que los 1's se propagaron a sus 
# vecinos con 0. Guardalo en un archivo propaga.py.

def propagar(lista):
    propagacion = []
    n = len(lista)-1
    for a, b in enumerate(lista):
        if b==-1:
            propagacion.append(b)
        if b == 0:
            propagacion.append(b)
        if b == 1:
            propagacion.append(b)
            if a < (n) and lista[a+1]==0:
                lista[a+1] = 1
    for c in range (n):
        if propagacion[n] == 1 and propagacion[n-1] == 0:
                propagacion[n-1] = 1
        n -= 1
    return propagacion


print (f'Propagación 1: {propagar([ -1*((i% 6)//2-1) for i in range(60) ])}.')
# devuelve: Propagación 1: [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1].

print (f'Propagación 2: {propagar([ (i% 6)//2-1 for i in range(200) ])}.')
# devuelve: Propagación 2: [1, 1, 1, 1, 1, 1].
