# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 20:30:54 2019

@author: barbara.barbosa
"""
"""
1) Faça um script para estimar o valor de π utilizando o método de Monte Carlo.
"""



import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x=np.random.rand (100000)
y=np.random.rand (100000)

d=(np.sqrt((0.5-x)**2)+((0.5-y)**2))

ac=d[d<=0.5]
x=len(ac)
pi=4*(x/100000)


print("o total de pontos que temos no circulo:",x)
print ("")
print("valor de pi",pi)


