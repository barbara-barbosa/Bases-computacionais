# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 20:30:54 2019

@author: barbara.barbosa
"""
"""
O índice de massa corporal (IMC) de uma pessoa é calculado por:

IMC=mh2
em que m é a massa corporal, em kg, e h é a altura, em metros.

O IMC tem a seguinte classificação:
menor que 17 kg/m2 -- Muito abaixo do peso
17 a 18,5 kg/m2 -- Abaixo do peso
18,5 a 25 kg/m2 -- Peso normal
25 a 30 kg/m2 -- Acima do peso
30 a 35 kg/m2 -- Obesidade Grau I
35 a 40 kg/m2 -- Obesidade Grau II
maior que 40 kg/m2 -- Obesidade Grau III
Escreva um script Python para calcular o IMC e mostrar a classificação do IMC. Teste para 
a) m=52 kg e h=1,58 m, b) m=83 kg e h=1,75 m, c) seu peso e altura
"""


m=52
h=1.58
i=(m/(h**2))
print("o IMC é",i,)
if i < 17 :
    
    print("Muito abaixo do peso")
else:
    if i >= 17 and i <= 18.5:
        print("Abaixo do peso")
        
    if i >=18.5 and i <= 25:
        print("Peso normal")
        
    if i >=25 and i <= 30:
        print("Acima do peso")
        
    if i >=30 and i <= 35:
        print("Obesidade Grau I")
         
    if i >=35 and i <= 40:
        print("Obesidade Grau II")
       
    if i > 40:
        print("Obesidade Grau III")
   
m=83
h=1.75
i=(m/(h**2))
print("o IMC é",i,)
if i < 17 :
    
    print("Muito abaixo do peso")
else:
    if i >= 17 and i <= 18.5:
        print("Abaixo do peso")
        
    if i >=18.5 and i <= 25:
        print("Peso normal")
        
    if i >=25 and i <= 30:
        print("Acima do peso")
        
    if i >=30 and i <= 35:
        print("Obesidade Grau I")
         
    if i >=35 and i <= 40:
        print("Obesidade Grau II")
       
    if i > 40:
        print("Obesidade Grau III")
        
m=58
h=1.66
i=(m/(h**2))
print("o IMC é",i,)
if i < 17 :
    
    print("Muito abaixo do peso")
else:
    if i >= 17 and i <= 18.5:
        print("Abaixo do peso")
        
    if i >=18.5 and i <= 25:
        print("Peso normal")
        
    if i >=25 and i <= 30:
        print("Acima do peso")
        
    if i >=30 and i <= 35:
        print("Obesidade Grau I")
         
    if i >=35 and i <= 40:
        print("Obesidade Grau II")
       
    if i > 40:
        print("Obesidade Grau III")
   
    
    
    """ acidez A(x) de uma solução de hidróxido de magnésio em ácido clorídrico,
    sob certas condições experimentais, é dada pela equação
    A(x)=x3+3x2−54
    na qual x é a concentração de íons hidrônio
    Pede-se:
        1) Gere o gráfico de A(x) em função de x para 0 ⩽x⩽8.
        2) Determine a concentração x do íon de hidrônio que resulta em solução saturada 
    (i.e., com acidez nula). Acrescente uma instrução que gere um ponto vermelho no gráfico 
    correspondente à saturação nula da solução.
    
    """
    
    
    import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0, 9, 1)
a=((x**3)+(3*(x**2))-54)
print (x)
print(a)
plt.figure()
plt.plot(x,a)
plt.plot(x[a==0],a[a==0],marker='d', color='red', linestyle='--')
print( )
plt.xlabel('X( Concentração x do íon )')
plt.ylabel('Y( Acidez)')
plt.grid()
plt.title('Grafico A(x))')
plt.show()


"""
3) Faça o gráfico de: f(x)=|x−2|+|2x+1|−x−6  
    Faça o gráfico com x variando de -10 a 10.
    Mostre no Console o menor valor de x tal que f(x)>0 e x>0.
    
"""

x=np.arange(-10, 11, 1)
f=(x-2)+(2*x+1)-x-6
print (x)
print(f)
plt.figure()
plt.plot(x,f)
i=x[f>0]
x = np.min(i)
print ()
print ("Menor valor de x tal que f(x)>0 e x>0 = ",x)
print( )
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.title('Grafico f(x))')
plt.show()


"""
4) Faça o gráfico da seguinte função: f(x)=x2–sin(0.784x2)–2
    Mostre no Console as raízes da função (i.e. os valores de x para os quais f(x)=0).
 
"""


x=np.arange(0, 11, 1)
f=(x**2)-(np.sin(0.784*(x**2)))-2
print (x)
print(f)
plt.figure()
plt.plot(x,f)
i=x[x==0]
x = np.min(i)
print ()
print ("Raizes da função F(x)=0 ",x)
print ("Não apresenta raizes")
print( )
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.title('Grafico F(x)')
plt.show()
