# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.

Autor: barbara.barbosa
"""

"""


1) Para este item você deverá usar o arquivo com todos os resultados do campeonato Brasileiro de futebol 
de 2018 (tabelaBrasileirao2018.csv encontrado na pasta aula5/dados) (dados obtidos desta e desta
        página da Wikipedia).

Calcule (e mostre o resultado na tela) a porcentagem de 
jogos que o time da casa (mandante) ganhou o jogo.

Calcule (e mostre o resultado na tela) a porcentagem de
 jogos que o time da casa (mandante) não perdeu o jogo.

"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


tab=pd.read_csv('tabelaBrasileirao2018.csv')

x=(tab['Placar do Mandante'])
y=tab['Placar do Mandante']> tab['Placar do Visitante']
win=len(y[y==True])
result=((win/x)*100)
print('A porcentagem de jogos que o time da casa (mandante) ganhou o jogo',result,'%')


x1=(tab['Placar do Mandante'])
y2=tab['Placar do Mandante'] >= tab['Placar do Visitante']
won=len(y2[y2==True])
result2=((won/x1)*100)
print('a porcentagem de jogos que o time da casa (mandante) não perdeu o jogo.',result2,'%')





"""
2) Para este item você deverá usar o arquivo com a taxa de inflação mensal (IGP-DI)
 no Brasil de fevereiro de 1944 a junho de 2019 (dados disponibilizados por Ipeadata).

Faça um gráfico da taxa de inflação mensal em função do tempo.
Mostre em que mês e ano e qual foi a maior taxa de inflação mensal 
medida neste período (fevereiro de 1944 a junho de 2019).
Dica: para fazer o gráfico, note que um mês corresponde a um doze avos de ano. 
Para facilitar a criação do gráfico você pode criar uma outra coluna que corresponda 
ao ano adicionado da fração correspondente ao mês.

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


inf = pd.read_csv('inflacaoMensal.csv')

plt.figure()
plt.title('Gráfico Taxa de Inflação ')
print('Taxa de inflação mensal')
plt.plot(inf['Ano'], inf['Inflação'])

n=np.max(inf['Inflação'])
ano=inf['Ano'].values[inf['Inflação']==n]
mes=inf['Mês'].values[inf['Inflação']==n]

print (inf)
print('A maior taxa de inflação foi no ano:' ,ano[0], ' e o mês', mes[0])
plt.xlabel('Tempo (anos)')
plt.ylabel('Taxa de Inflação')    


plt.show()


"""

3) Para este item você pode usar esse histórico de visualização do Netflix ou,
 se você tiver acesso ao Netflix, usar o seu histórico
 (após entrar com a sua senha, role até o final da página e
 clique em "Baixar tudo").

Mostre quais são os 10 programas mais vistos.
Em qual mês do ano foi assistido mais programas?
Sugestão: No seu script, depois do comando para
 carregar o arquivo, coloque a seguinte sequência de instruções:
 
data['Categoria'] = 'Filme'  
data['Categoria'][data['Title'].str.contains(": Temporada|: Stranger|: Parte")] = 'Série'  
data['Programa'] = data['Title']  
data[['Programa','Episódio']] = data[data['Categoria']=='Série']['Title'].str.split(pat = ': Temporada|: Stranger Things|: Parte', expand = True, n = 1)   
data.loc[data['Categoria']=='Filme', 'Programa'] = data.loc[data['Categoria']=='Filme', 'Title']  
data = data.drop(columns = 'Title')
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('netflix.csv')

data['Categoria'] = 'Filme'  
data['Categoria'][data['Title'].str.contains(": Temporada|: Stranger|: Parte")] = 'Série'  
data['Programa'] = data['Title']  
data[['Programa','Episódio']] = data[data['Categoria']=='Série']['Title'].str.split(pat = ': Temporada|: Stranger Things|: Parte', expand = True, n = 1)   
data.loc[data['Categoria']=='Filme', 'Programa'] = data.loc[data['Categoria']=='Filme', 'Title']  
data = data.drop(columns = 'Title')

data['Date'] = pd.to_datetime(data['Date'], format = '%d/%m/%Y')
data = data.sort_values(['Date', 'Programa'])
print(data['Date'].dt.year)
print(data['Date'].dt.month)
print('TOP 10 Programas mais assistidos:',data['Programa'].value_counts().head(10))
print(' ')
print('Mês do ano foi assistido mais programas/Quantos programas foram assistidos:',data['Date'].dt.month.value_counts().head(1))






