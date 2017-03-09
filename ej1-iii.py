# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:14:36 2017

Los factores primos en 13195 son 5, 7, 13 y 29 ¿ Cuál es el factor primo más grande en el número 600851475143 ?

@author: ger
"""

from math import *

# hallar primos menores que la raiz cuadrada de 600851475143 (pequeño teorema de Fermat)

primos = []
lim = ceil(sqrt(600851475143))

for i in range(1,lim,2):
    divisible = 0
    for j in range(3,ceil(sqrt(i))):
        if i%j == 0:
            divisible = 1
            break
    if divisible == 0:
        primos.append(i)
    print(i,'/',lim)
   

# ahora buscamos los factores primos de 600851475143
factores_primos = []

for i in primos:
    if 600851475143%i == 0:
        factores_primos.append(i)
        
print('Factor primo más grande en el número 600851475143:', max(factores_primos))