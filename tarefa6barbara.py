# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

"""
1) A tensão elétrica medida em um circuito, em volts, 
tem a seguinte expressão no instante t, em segundos:
v(t)=e−0.5tcos(2π0.8t)
Faça o gráfico da altura em função do tempo.
Sugestão: fazer o gráfico com tempo entre 0 e 10 s com incremento de 0.05 s.
"""

import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0, 10, 0.05)
v=(np.exp(-0.5*t))*(np.cos((2*np.pi)*(8*t)))
print (t)
print(v)
plt.figure()
plt.plot(t,v)
print( )
plt.xlabel('X( Tempo em segundos)')
plt.ylabel('Y( Tensão eletrica em volts)')
plt.title('Grafico V(T)')
plt.show()

"""
2) Faça um gráfico da equivalência da temperatura em Fahrenheits em função da temperatura
    em Celsius:
F=95C+32
Faça o gráfico tomando 100 pontos entre -20 ∘C e 100 ∘C.
"""

c = np.linspace(-20, 100, 100)
f=(1.8*c)+32
print (c)
print(f)
plt.figure()
plt.plot(c,f)
print( )
plt.xlabel('X(Temperatura em Fahrenheits)')
plt.ylabel('Y(Temperatura em Celsius)')
plt.title('Grafico TF(TC)')
plt.show()

"""
3) A população de uma cidade cresce aproximadamente de acordo com a seguinte função:
P(a)=800000ea−199440
em que a é o ano e P é o número de habitantes.

Faça o gráfico do número de habitantes entre 1994 e 2020.

Mostre no Console qual a previsão do número de habitantes desta cidade em 2020.
"""

a= np.arange(1994, 2020, 1)
p=800000*(np.exp((a-1994)/40))
print(a)
print(p)
plt.figure()
plt.plot(a,p)
print( )
x = np.max(p)
print( )
print('A previsão de habitantes para o ano de 2020 é', x,'pessoas')
plt.xlabel('X(Anos)')
plt.ylabel('Y(Número de habitantes)')
plt.title('Grafico P(A)')
plt.show()




