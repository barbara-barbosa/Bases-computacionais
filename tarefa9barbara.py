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
1) Para este item você deverá usar o arquivo com a porcentagem da população
 brasileira que é analfabeta, dividida por unidade da federação, de 1981 a 2014 
 (analfabetismo.csv, encontrado na pasta aula5/dados) (dados disponibilizados por Ipeadata).

Faça um gráfico da taxa de analfabetismo em São Paulo em função do tempo (anos).
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


Analfabetismo = pd.read_csv('analfabetismo.csv')


plt.figure()
print()
print(' Gráfico da taxa de analfabetismo')
plt.plot(Analfabetismo['São Paulo'], Analfabetismo['Ano'])
plt.xlabel('Taxa de Analfabetismo')
plt.ylabel('Tempo (anos)')
plt.show()         

plt.show()

