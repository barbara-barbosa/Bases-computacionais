# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

"""
1) Faça uma função que receba um número a, um número b e um número x. Esta função deve retornar True 
    se x estiver entre a e b e False caso contrário. 
    Além disso a função deve mostrar uma mensagem dizendo se x está no intervalo entre a e b ou não.

Teste para

a) a = -2.5, b = 6.3 e x = 9.1;
b) a = -10, b = 7 e x = 2.2
c) a = 67.2, b = 87.2 e x = 8.1
Sugestão:

a função pode ter a seguinte estrutura:

def estaNoIntervalo(a, b, x):
    ...
    return resposta
    
"""
import numpy as np

def estanointervalo (a, b, x):
    
    verifica = a<= x and b >= x
    if verifica : 
        print (' X esta entre A e B')
    else:
        print (' X não esta entre  A e B')
    
    return verifica

print ( "para A= -2.5 e B= 6.3, x=9.1")
a1=-2.5
b1=6.3
x1=9.1

estanointervalo(a1,b1,x1)

a2=-10
b2=7
x2=2.2

print ( "para A= -10 e B= 7, x=2.2")
estanointervalo(a2,b2,x2)


a3=67.2
b3=87.2
x3=8.1

print ( "para A= 67.2 e B= 87.2, x=8.1")
estanointervalo(a3,b3,x3)

  