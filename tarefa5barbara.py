# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
'''
Uma bola é lançada ao ar. Suponha que sua altura h(t), em metros, t segundos após o lançamento, seja:
    h(t)=−t2+4t
 
a) Faça o gráfico da altura em função do tempo. Não se esqueça de indicar o significado de cada eixo, colocando a unidade da altura e do tempo.

b) A altura máxima atingida pela bola.
    Sugestão: fazer o gráfico com o tempo entre 0 s e 5 s com incremento de 0.1 s.
    '''
import numpy as np
import matplotlib.pyplot as plt



t=np.arange(0,5,0.1)

y=-t**2+4*t
print (t)
print(y)
plt.figure()
plt.plot(t,y)
y = np.max(y)
print( )
print('A altura maxima é', y,'metros')
plt.xlabel('T(tempo em s)')
plt.ylabel('Y(altura em m)')
plt.title('Grafico H(T)')
plt.show()



