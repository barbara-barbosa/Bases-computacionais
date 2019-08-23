# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 20:30:54 2019

@author: barbara.barbosa
"""
"""
1) Faça um script para estimar o valor de π utilizando o método de Monte Carlo.0
"""



import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

N=100000
x=np.random.rand(N)
y=np.random.rand(N)

d=np.sqrt((0.5-x)**2+(0.5-y)**2)

ac=d[d<=0.5]
x=len(ac)
pi=4*(x/N)


print("o total de pontos que temos no circulo:",x)
print ("")
print("valor de pi",pi)


