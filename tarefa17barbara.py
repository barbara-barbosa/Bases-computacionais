# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

"""
1) Faça uma função que recebe dois vetores ou duas colunas de uma DataFrame do Pandas e retorne
 a correlação r. A função deve estar no mesmo arquivo que a função que calcula a regressão.
 Esse arquivo deve ser importado no script que executará o teste abaixo.

Teste com o dado de público e o dado da renda dos jogos do campeonato brasileiro de 2018 e 
mostre a correlação encontrada.
    
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


def corr(x, y):
   
    mediaX = np.mean(x)
    mediaY = np.mean(y)
    desvioX = x - mediaX
    desvioY = y - mediaY
    r=((np.sum(desvioX*desvioY))/(((np.sqrt(np.sum(desvioX**2))))*((np.sqrt(np.sum(desvioY**2))))))
    print(r)
    return r



tab = pd.read_csv('tabelaBrasileirao2018.csv')
corr(tab['Público'],tab['Renda (R$)'])
