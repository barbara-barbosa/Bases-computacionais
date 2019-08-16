# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

"""
Este programa Calcula o volume de uma esfera com raio contida em uma variavel
"""
"""
1) Faça uma função que receba um vetor t,um valor A, um valor b e um valor c e retorne um outro vetor x.

x(t)=A1+bt2−−−−−−√+c
Além disso a função deve plotar o gráfico de x em função de t.

Teste para

a) t indo de 0 a 10 com 1000 pontos, A = 2, b = 0.5, c = 0;
b) t indo de 0 a 15 com intervalo de 0.2 entre os valores do vetor, A = 10, b = 0.2, c = 1
c) t indo de -0,5 a 0,5 com 500 pontos, A = -3, b = -1.5, c = -10;


"""
import matplotlib.pyplot as plt
import numpy as np

print('EXERCICIO 1')

def volume (a, b, t, c):
    
    x = a*(np.sqrt(1+(b*(t*t))))+c
    
    
    return x

print ("")
a1=2
b1=0.5
t1=np.linspace(0.1, 10, 1000)
c1=0

x1= volume (a1,b1,t1,c1)


plt.figure()
plt.xlabel('x')
plt.ylabel('t')
plt.title('a) - Gráfico de x em função de t')
plt.plot(x1, t1)


print ("")
a2=2
b2=0.5
t2=np.arange(0, 15, 0.2)
c2=0

x2= volume (a2,b2,t2,c2)


plt.figure()
plt.xlabel('x')
plt.ylabel('t')
plt.title('b) - Gráfico de x em função de t')
plt.plot(x2, t2)

print ("")
a3=10
b3=0.2
t3=np.linspace(-0.5, 0.5, 500)
c3=-10

x3= volume (a3,b3,t3,c3)
print (x3)

plt.figure()
plt.xlabel('x')
plt.ylabel('t')
plt.title('c) - Gráfico de x em função de t')
plt.plot(x3, t3)


"""
2) Faça uma função que ao ser executada sorteia um número entre 0 e 1. 
Se esse número for menor do que 0,5 apareça na tela a mensagem 'Cara'. 
Se esse número for maior do que 0,5 apareça a mensagem 'Coroa'.
 Uma sugestão do nome da função é 'cara_ou_coroa'.

Teste a função chamando 10 vezes a função que você fez.

Dica: o comando 'np.random.rand(n)' gera n números aleatórios entre 0 e 1.
"""


import matplotlib.pyplot as plt
import numpy as np
import random

print('EXERCICIO 2')
def cara_ou_coroa (n):
    
    verifica = 0.5<= n 
    if verifica : 
        print (' Cara ')
    else:
        print (' Coroa ')
    
    return verifica

print('valores gerados:')

x = np.random.rand(10) 
    
for i in range(len(x)):
    print(x[i])
    

n1 = cara_ou_coroa (random.choice(x))
n2 = cara_ou_coroa (random.choice(x))
n3 = cara_ou_coroa (random.choice(x))
n4 = cara_ou_coroa (random.choice(x))
n5 = cara_ou_coroa (random.choice(x))
n6 = cara_ou_coroa (random.choice(x))
n7 = cara_ou_coroa (random.choice(x))
n8 = cara_ou_coroa (random.choice(x))
n9 = cara_ou_coroa (random.choice(x))
n10 = cara_ou_coroa (random.choice(x))

"""
4) Dados valores x1, y1, x2, y2, sendo esses valores das coordenadas (x1,y1) e (x2,y2)
    de dois pontos.

Fazer uma função que encontre a inclinação da reta m e o ponto b em que a reta
 cruza o eixo y da reta y=mx+b que passa pelos dois pontos. Além disso deve ser feito o 
 gráfico da reta encontrada com N pontos, além de mostrar os dois pontos dados como entrada,
 indicados com marcadores quadrados.

Essa função deve retornar m e b e receber como parâmetros x1, y1, x2, y2 e N.

Dica: a inclinação de uma reta, dados dois pontos é:

m=y2−y1x2−x1
e o ponto que cruza o eixo y é:

b=y1−mx1
Teste para:

a) x1 = -19, y1 = 2, x2 = 10, y2 = -10, N = 1000
b) x1 = -2, y1 = 8, x2 = 20, y2 = 43, N = 2000
c) x1 = 7, y1 = 13, x2 = 1, y2 = 2, N = 500
"""

import matplotlib.pyplot as plt
import numpy as np

print('EXERCICIO 4')
def calcula(x1, y1, x2, y2, n):
    m = (y2-y1)/(x2-x1)
    b = y1-(m*x1)
    
    return m, b


x11=-19
y11=2
x22=10
y22=-10
n1=1000
m1, b1 = calcula(x11, y11, x22, y22, n1 )
print('m = ', m1, 'b = ', b1)

plt.figure()
plt.xlabel('x')
plt.ylabel('t')
plt.title('a) - Inclinação da reta')
plt.plot(b1, m1 , marker='d', color='red', linestyle='--')
plt.plot(n1, m1)

x21=-19
y21=2
x32=10
y32=-10
n2=2000
m2, b2 = calcula(x21, y11, x32, y32, n2 )
print('m = ', m2, 'b = ', b2)

plt.figure()
plt.xlabel('x')
plt.ylabel('t')
plt.title('b) - Inclinação da reta')
plt.plot(b2, m2 , marker='d', color='red', linestyle='--')
plt.plot(n2, m2)

x31=7
y31=13
x42=1
y42=2
n3=500
m3, b3 = calcula(x31, y31, x42, y42, n3 )
print('m = ', m3, 'b = ', b3)

plt.figure()
plt.xlabel('x')
plt.ylabel('t')
plt.title('c) - Inclinação da reta')
plt.plot(b3, m3 , marker='d', color='red', linestyle='--')
plt.plot(n3, m3)





"""
3) Faça uma função que retorne a moda (ver aula 7) de uma coluna de um DataFrame do Pandas. 
    As entradas devem ser o DataFrame do Pandas e o nome da coluna.
    Além de retornar a moda, a função deve mostrar na tela qual é a moda encontrada

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

inf = pd.read_csv('tabelaBrasileirao2018.csv')
print('EXERCICIO 3')
def moda(x):
    
    
    m = inf[x].mode()
    
    return m


    
print ('Não esqueca de digitar exatamente igual, respeitando os acentos e as letras maisculas')
x1=input('Digite o nome da coluna que deseja ver a moda - Data - Turno - Árbitro :' )

m1 = moda(x1)

print('A moda da coluna  é', m1)




