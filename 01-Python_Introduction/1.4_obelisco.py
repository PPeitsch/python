# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 05:42:12 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.4

"""

print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.4\n')

grosor_billete = 0.11 * 0.001   # 0.11 mm en metros
altura_obelisco = 67.5          # altura en metros
num_billetes = 1
dia = 1

while num_billetes * grosor_billete <= altura_obelisco:
    print(dia, 'días\t\t', num_billetes, 'billetes\t\t', round(num_billetes * grosor_billete, 2), 'metros')
    dia += 1
    num_billetes = num_billetes * 2

print('\nPasaron', dia, 'días')
print('Y la cantidad de billetes acumulados es:', num_billetes)
print('Con una altura total de', round(num_billetes * grosor_billete, 2), 'metros')



"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.4

1 días		 1 billetes		 0.0 metros
2 días		 2 billetes		 0.0 metros
3 días		 4 billetes		 0.0 metros
4 días		 8 billetes		 0.0 metros
5 días		 16 billetes		 0.0 metros
6 días		 32 billetes		 0.0 metros
7 días		 64 billetes		 0.01 metros
8 días		 128 billetes		 0.01 metros
9 días		 256 billetes		 0.03 metros
10 días		 512 billetes		 0.06 metros
11 días		 1024 billetes		 0.11 metros
12 días		 2048 billetes		 0.23 metros
13 días		 4096 billetes		 0.45 metros
14 días		 8192 billetes		 0.9 metros
15 días		 16384 billetes		 1.8 metros
16 días		 32768 billetes		 3.6 metros
17 días		 65536 billetes		 7.21 metros
18 días		 131072 billetes		 14.42 metros
19 días		 262144 billetes		 28.84 metros
20 días		 524288 billetes		 57.67 metros

Pasaron 21 días
Y la cantidad de billetes acumulados es: 1048576
Con una altura total de 115.34 metros

""" 