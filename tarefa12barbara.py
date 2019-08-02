# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.

Autor: barbara.barbosa
"""

"""


 Faça a aproximação de π usando a fórmula de Leibniz:

π≈4−43+45−47+49+...
Calcule (e mostre na tela) a aproximação de π considerando 
a) 50 termos, b) 500 termos, c) 1000 termos e d) 10000 termos.

Dica: Note que o sinal do termo muda a cada termo.
 Talvez verificar se o i é par ou ímpar ajude a decidir
 se para aquele i o sinal é mais ou menos.
"""

import numpy as np
import matplotlib.pyplot as plt

def calculandopi(n):
    pi=0
    x=4 
    
    for i in range(n):
        result = (2*i+1)
        termo = x/result
        if i%2:
            pi -= termo
        else:
            pi += termo
    return(pi)


print ('Para 50 termos o valor de Pi:',calculandopi(50))
print ('Para 500 termos o valor de Pi:',calculandopi(500))
print ('Para 1000 termos o valor de Pi:',calculandopi(1000))
print ('Para 10000 termos o valor de Pi:',calculandopi(10000))



"""
2) Para este item você deverá usar o arquivo com a taxa de inflação mensal (IGP-DI)
    no Brasil de fevereiro de 1944 a junho de 2019 (dados disponibilizados por Ipeadata).

Faça um gráfico com a taxa de inflação anual em função dos anos, de 1945 a 2018.
Sugestões: Crie um outro DataFrame com um campo com a inflação anual e um outro campo
 com o ano. Outra opção é criar um vetor do Numpy com os anos e um outro vetor do Numpy
 com a taxa de inflação anual calculada.

Lembre-se de que o dado da inflação mensal é o aumento de preço em relação ao mês anterior.

Portanto, o índice de inflação anual, dado os índices de inflação mensais em %, é:

Inf=[(1+Inf1100).(1+Inf2100)...(1+Inf12100)−1].100

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

inf = pd.read_csv('inflacaoMensal.csv')

anos = np.arange (1994,2019,1)

colunas = ['Inflação']
x = pd.DataFrame(0, index=np.arange(1994, 2019, 1), columns=colunas)
x['Anos'] = anos
x


plt.figure()
plt.title('Gráfico Taxa de Inflação ')
print('Taxa de inflação mensal')
plt.plot(inf['Ano'], inf['Mês'])



"""
3) Calcular a aproximação de uma onda quadrada seguindo a seguinte expressão
(a expressão abaixo é calculada utilizando uma teoria matemática conhecida como 
 série de Fourier):

x(t)≈4π∑i=1Nsin[(2i−1)t]2i−1
Faça a aproximação para 0⩽t⩽10 
(utilize um número suficiente de pontos no vetor t para poder observar 
 o gráfico de x(t), algo em torno de 100000 pontos).

Faça a aproximação para a) N = 10, b) N = 100, c) N = 1000 e
 d) N = 10000. Coloque todas as aproximações em um único gráfico,
 com a aproximação de x(t) em função de t.

Dica: se você estiver com dificuldade, faça primeiro o 
gráfico considerando i = 1, sem nenhuma somatória (N = 1). 
Depois disso, coloque o código que você tiver escrito dentro de um 
for ou while para variar o valor de i.

"""

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


x = np.arange (10)
t = np.arange (0,10,1)

cal= (np.pi/4)*( (np.sin(2.0[i]-1)*t) 

    


plt.title(' serie de Forrie ')
plt.xlabel('X metros')
plt.ylabel('T segundos') 
plt.grid()
plt.plot(cal, t)

"""