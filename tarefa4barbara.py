# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

"""
Este programa Calcula o volume de uma esfera com raio contida em uma variavel
"""

print('Exercico 1-Volume das esferas')

r1=0.32
r2=1
r3=1.9

import numpy as np


r=((4/3)*np.pi*(r1**3))
print ( 'Para raio de 0,32 m, o volume da esfera é',(r),'m')

r=((4/3)*np.pi*(r2**3))
print ( 'Para raio de 1 m, o volume da esfera é',(r),'m')

r=((4/3)*np.pi*(r3**3))
print ( 'Para raio de 1,9 m, o volume da esfera é',(r),'m')


"""
Este programa calcula Fahrenheit dada a temperatura em Celsius contida em uma variavel Tc"

"""
print (' ')
print('Exercico 2-Conversao de temperatura')

t1=-10
t2=30
t3=5

import numpy as np


tc= (t1*(9/5)+32)
print ( 'Para temperatura de -10º graus, corresponde em ' , (tc),'F')

tc= (t2*(9/5)+32)
print ( 'Para temperatura de 30º graus, corresponde em ' , (tc),'F')

tc= (t3*(9/5)+32)
print ( 'Para temperatura de 5º graus, corresponde em ' , (tc),'F')



"""
Este programa calcula o tamanho do lado c de um triângulo com lados a,b e ângulo θ entre os lados a e b conhecidos
. a, b e θ devem estar gravadas em variáveis. A expressão para isso é conhecida como lei dos cossenos:
c=a2+b2−2abcos(θ)−−−−−−−−−−−−−−−√

"""
print (' ')
print('Exercico 3-lei dos cossenos')

a1=1
b1=2
x1=0

a2=3
b2=1
x2=45

a3=10
b3=11
x3=15

import numpy as np

c=(np.sqrt((a1**2+b1**2)-(2*a1*b1*np.cos(x1))))
print ('Um triangulo de lado a=1 b=2 e angulo de 0 graus, tem o lado c com o tamanho de',(c),'m')

c=(np.sqrt((a2**2+b2**2)-(2*a2*b2*np.cos(x2))))
print ('Um triangulo de lado a=3 b=1 e angulo de 45graus, tem o lado c com o tamanho de',(c),'m')

c=(np.sqrt((a3**2+b3**2)-(2*a3*b3*np.cos(x3))))
print ('Um triangulo de lado a=10 b=11 e angulo de 15graus, tem o lado c com o tamanho de',(c),'m')


"""
Este programa calcula O i-ésimo número pela série de Fibonacci
"""

print (' ')
print('Exercico 4-série de Fibonacci')

i1=30
i2=31
i3=32

import numpy as np

z=(((1+(np.sqrt(5)))/2)**i1)
z1=(((1-(np.sqrt(5)))/2)**i1)
z2=np.sqrt(5)
i=((z-z1)/z2)

print ('Serie de Fibonacci, para i=30',(np.floor(i)),)

z=(((1+(np.sqrt(5)))/2)**i2)
z1=(((1-(np.sqrt(5)))/2)**i2)
z2=np.sqrt(5)

i=((z-z1)/z2)
print ('Serie de Fibonacci, para i=31',(np.floor(i)),)

z=(((1+(np.sqrt(5)))/2)**i3)
z1=(((1-(np.sqrt(5)))/2)**i3)
z2=np.sqrt(5)

i=((z-z1)/z2)
print ('Serie de Fibonacci, para i=32',(np.floor(i)),)




