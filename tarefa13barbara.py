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
1) Para este item você deverá usar o arquivo com todos os resultados do campeonato Brasileiro de 
futebol de 2018 (tabelaBrasileirao2018.csv encontrado na pasta aula7/dados) (dados obtidos desta e 
desta página da Wikipedia).

Escolha um time e faça o histograma da distribuição do público nos jogos em que este 
time foi o mandante.

Calcule qual foi o público médio nos jogos em que o time escolhido foi o mandante.






"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

inf = pd.read_csv('tabelaBrasileirao2018.csv')
inf.head()



mediaPúblicoCorinthians = inf[inf['Mandante']=='Corinthians']['Público'].mean()
print('A media do publico do corinthians é',mediaPúblicoCorinthians)




plt.title('distribuição do público nos jogos do Corinthians')
mediaPúblicoCorinthians=inf[inf['Mandante']=='Corinthians']['Público'].hist()


















