# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 05:59:33 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.11: Calculadora de Adelantos - Bonus

Corregí el código anterior de forma que el pago del último
mes se ajuste a lo adeudado.

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.11: Calculadora de Adelantos - Bonus\n')

# Declaración de variables
i = 0
tasa = 0.0
pagado = 0.0
pago_extra_mes_comienzo = 0
pago_extra_mes_fin = 0
pago_extra = 0
cuota_intento = 0

# Monto del préstamo
saldo = input('Ingrese el monto que desea solicitar: ')
# Convierto el string a entero
saldo = int(saldo)

# Plazo de devolución, en años
plazo = input('Ingrese el plazo, en años, de devolucion: ')
# Convierto el string ingresado en entero
plazo = int(plazo)
# Convierto el plazo a meses
plazo *= 12

if plazo == 360:
    tasa = 0.05

# Informo el % de tasa anual
print('La tasa anual sera de:', tasa*100, '%')

# Valor de la cuota fija, según el interés
cuota = 2684.11
print('El valor de la cuota fija será de:', cuota)


# Intento 1 de calculo de la cuota
#for i in range(plazo):
#    cuota_intento += saldo * tasa/12
#print('El valor de la cuota fija (intento) será de:', cuota_intento)

# Intento 2 de calculo de la cuota
#cuota_intento = saldo * ( (tasa * ((1 + tasa)**plazo)) / (((1 + tasa)**plazo) - 1) )
#print('El valor de la cuota fija (intento) será de:', cuota_intento)


# Pregunto el monto de cada adelanto mensual
pago_extra = input('Cual es el monto mensual a adelantar? ')
# Convierto el string ingresado en entero
pago_extra = int(pago_extra)

# Mes de comienzo de los adelantos
pago_extra_mes_comienzo = input('En qué mes comienza a realizar adelantos? ')
# Convierto el string ingresado en entero
pago_extra_mes_comienzo = int(pago_extra_mes_comienzo)


# Durante cuantas cuotas va a realizar el adelanto
pago_extra_mes_fin = input('En qué cuota finaliza los adelantos? ')
# Convierto el string ingresado en entero
pago_extra_mes_fin = int(pago_extra_mes_fin)

# Un salto de linea para separar la tabla
print('\n')
print('Cuota\tPagado\t\tSaldo')

i = 0
# Calculo de costo final descontando los adelantos
while saldo > 0:
    saldo = saldo * (1 + tasa/12) - cuota
    pagado += cuota
    i += 1
    
    if i >= pago_extra_mes_comienzo and i <= pago_extra_mes_fin:
        saldo -= pago_extra
        pagado += pago_extra
    print(i, '\t\t', round(pagado, 2), '\t', round(saldo, 2))
    if saldo < cuota:
        pagado += saldo
        saldo -= saldo
        i += 1
        print(i, '\t\t', round(pagado, 2), '\t', round(saldo, 2))


print('\nEl monto total pagado es:', round(pagado, 2))
print('En un total de', i, 'meses')

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.11: Calculadora de Adelantos - Bonus


Ingrese el monto que desea solicitar: 500000

Ingrese el plazo, en años, de devolucion: 30
La tasa anual sera de: 5.0 %
El valor de la cuota fija será de: 2684.11

Cual es el monto mensual a adelantar? 1000

En qué mes comienza a realizar adelantos? 61

En qué cuota finaliza los adelantos? 108

Cuota	Pagado		Saldo
1 		 2684.11 	 499399.22
2 		 5368.22 	 498795.94
3 		 8052.33 	 498190.15
4 		 10736.44 	 497581.83
5 		 13420.55 	 496970.98
6 		 16104.66 	 496357.58
7 		 18788.77 	 495741.63
8 		 21472.88 	 495123.11
9 		 24156.99 	 494502.01
10 		 26841.1 	 493878.33

...          ...          ...

300 		 853233.0 	 24440.8
301 		 855917.11 	 21858.53
302 		 858601.22 	 19265.5
303 		 861285.33 	 16661.66
304 		 863969.44 	 14046.97
305 		 866653.55 	 11421.39
306 		 869337.66 	 8784.87
307 		 872021.77 	 6137.36
308 		 874705.88 	 3478.83
309 		 877389.99 	 809.21
310 		 878199.2 	 0.0

El monto total pagado es: 878199.2
En un total de 310 meses

""" 