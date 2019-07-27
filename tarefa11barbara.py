# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:31:55 2019

@author: barbara.barbosa
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:07:07 2019

@author: barbara.barbosa
"""

"""
1) Três séries, v,y e t seguem as seguintes regras:
v[i]=v[i−1]+0,01.(−9,81)
y[i]=y[i−1]+0,01v[i−1]
t[i]=t[i−1]+0,01
Começando com v[0] = 10 m/s, y[0] = 0 m e t[0] = 0 s, calcule os 250 primeiros valores das três séries.

Faça os gráficos com os valores encontrados de y em função de t e dos valores encontrados de v em
 função de t.

Observação: o cálculo destas três séries é uma simulação computacional para calcular a posição e 
velocidade de uma partícula lançada na vertical com velocidade
 inicial de 10 m/s. O método utilizado para realizar esta simulação é conhecido como método de Euler.

"""

import numpy as np
import matplotlib.pyplot as plt

v = np.zeros((250))
y = np.zeros((250))
t = np.zeros((250))

v[0] = 10
y[0] = 0
t[0] = 0

for i in range(1, 250, 1):

        v[i]=(v[i-1]+0.01*(-9.81))
         
        y[i]=(y[i-1]+(0.01)*(v[i-1]))
                
        t[i]=(t[i-1]+0.01)
        
plt.figure()
plt.title(' T em função de Y ')
plt.xlabel('t metros')
plt.ylabel('y segundos') 
plt.grid()
plt.plot(t, y)



plt.figure()
plt.title(' v em função de t ')
plt.xlabel('V metros')
plt.ylabel('T segundos') 
plt.grid()
plt.plot(v, t)



    
print('v = ',v)
print('y = ',y)
print('t = ',y)