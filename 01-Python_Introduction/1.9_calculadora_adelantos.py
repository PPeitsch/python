# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 01:19:33 2021

@author: Pablo Reynoso Peitsch

Programación en Python
-> Ejercicio 1.9: Calculadora de Adelantos

¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años,
comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?

"""

# Print Autor, Materia, Ejercicio
print('\nAutor: Pablo Reynoso Peitsch')
print('Materia: Programación en Python')
print('Ejercicio: 1.9: Calculadora de Adelantos\n')

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

i = 0
# Calculo de costo final descontando los adelantos
while saldo > 0:
    saldo = saldo * (1 + tasa/12) - cuota
    pagado = pagado + cuota
    i += 1
    
    if i >= pago_extra_mes_comienzo and i <= pago_extra_mes_fin:
        saldo = saldo - pago_extra
        pagado = pagado + pago_extra

print('El monto total pagado es:', round(pagado, 2))
print('En un total de', i, 'meses')

"""
RESULTADO:

Autor: Pablo Reynoso Peitsch
Materia: Programación en Python
Ejercicio: 1.9: Calculadora de Adelantos


Ingrese el monto que desea solicitar: 500000

Ingrese el plazo, en años, de devolucion: 30
La tasa anual sera de: 5.0 %
El valor de la cuota fija será de: 2684.11

Cual es el monto mensual a adelantar? 1000

En qué mes comienza a realizar adelantos? 61

En qué cuota finaliza los adelantos? 108
El monto total pagado es: 880074.1
En un total de 310 meses

""" 