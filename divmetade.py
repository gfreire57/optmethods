"""Divisão pela metade - EMA013 Métodos de otimização
Autor: Gabriel Hasmann
Data: 06/10/2021
Atualizado: 16/10/2021
-----------------------------------------------------------"""
import matplotlib.pyplot as plt
import time
import numpy as np
import math as mt

print('-> Método da divisão pela metade')

# Função que avalia o valor de y(x) em um ponto (facilita a organização do código)
def fun(x):
    # Inserir função a ser estudada
    y = -(1/(x-1)**2) * (mt.log(x)-2*(x-1)/(x+1))
    return y

# Inserir valores do intervalo inicial e precisão)
a = 1.5
b = 4
e = 2/21
L0 = b - a

k = 0  # variável para contar as iterações
while True:
    L = b - a
    k = k + 1
    print(f'----IT {k}----')
    l = L / L0 #variável criada somente para plotar na janela de comando usando print abaixo
    # print(f'L={L}, L0={L0}, então L/L0 = {l}')
    if L / L0 <= e:
        x_ymin=x[f.index(min(f))]
        print('\n\n\n-----RESULTADO-----')
        print(f'Parada na {k}a iteração\nymin={min(f):.4f} para x={x_ymin}')
        break
        # Caso a razão L/L0 seja menor que a precisão, programa para de executar
    x = np.array([a + L * 1 / 2, a + L / 4, a + L * 3 / 4])  # x0, x1, x2
    f = [fun(x[i]) for i in range(3)]  # valores de f(xn)
    print(f"a: {a}, b: {b}"
          f"\nL: {L}\n"
          f"  x1: {x[1]:.4f} ---   x0: {x[0]:.4f} ---   x2: {x[2]:.4f}\n"
          f"f_x1: {f[1]:.4f} --- f_x0: {f[0]:.4f} --- f_x2: {f[2]:.4f}")

    if f[2] >= f[0] > f[1]:
        b = x[0]
        x[0] = x[1]
    elif f[2] < f[0] <= f[1]:
        a = x[0]
        x[0] = x[2]
    elif f[1] > f[0] and f[2] > f[0] or f[1] == f[2]:
        a = x[1]
        b = x[2]

    '''print(f"Depois: \na: {a} - b: {b}\n"
          f"L: {L}, e: {e}")'''
    time.sleep(0.1)
    print('\n')