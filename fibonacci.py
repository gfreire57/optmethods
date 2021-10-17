"""Fibonacci - EMA013 Métodos de otimização
Autor: Gabriel Hasmann
Data: 14/10/2021
Atualizado: 15/10/2021
-----------------------------------------------------------"""
import time
import numpy as np
import math as mt

print('-> Método de Fibonacci')

'''Valores de entrada e função minimizada'''
# f: função a ser minimizada (inserida na função fun(x))


# Função em python que avalia o valor de y em um dado ponto x (facilita a organização do código)
def fun(x):
    # Inserir função a ser estudada
    #y = 0.1 + 0.1 * x + x ** 2 / (0.1 + x ** 2)
    f = -(1 / (x - 1) ** 2) * (mt.log(x) - 2 * (x - 1) / (x + 1))
    return f

# Cria automaticamente array com valores de fibonacci que serão usados no programa
def fib_minval(x):  # x: valor minimo do maior valor de uma sequencia de fibonacci
    Fib = np.array([0, 1])
    count = 2
    while max(Fib) < x:
        val = Fib[count - 1] + Fib[count - 2]
        Fib = np.append(Fib, val)
        count = count + 1
    Fib = np.delete(Fib, 0)  # deleta primeiro elemento da sequência criada dado que vale zero.
    return Fib

# Inserir valores do intervalo inicial e precisão
a = 1.5
b = 4
e = 2/21  # Precisão. Nesse caso, de 10%

# Carregar array dos valores da seq de fibo que serão usados
Fn = 1 / e  # valor mínimo do maior valor da sequencia
fib = fib_minval(Fn) #array com valores da seq de fibonacci
n = len(fib)-1 # tamanho da seq

# Intervalo de incerteza inicial e intervalo
L0 =  b-a
Lj = L0

j = 2  # variável para contar as iterações
while True:
    print(f'----IT {j}----')
    # print(f'Razão dessa iteração: {fib[n - j]} / {fib[n - j + 2]}')
    Lj_pto = (fib[n - j] / fib[n - j + 2]) * Lj
    print(f'Lj* = {Lj_pto}')
    # Valores de x e respectivos f(x)
    x1 = a + Lj_pto
    fx1 = fun(x1)
    x2 = b - Lj_pto
    fx2 = fun(x2)

    # print(f"Antes:\n-> a: {a:.4f}| x1: {x1:.4f} | x2: {x2:.4f}| b: {b:.4f}\n"
    #       f"              fx1: {fx1:.4f}  |fx2: {fx2:.4f}")
    if fx2 > fx1:
        b = x2
    else:
        a = x1
    Lj = b - a # atualiza valor de Lj
    print(f"  a: {a:.4f}   |  b: {b:.4f}\nfx1: {fx1:.4f}  |fx2: {fx2:.4f}")
    print(f'Lj = {Lj}')

    if Lj/L0 < e:
        print('\n\n\n-----RESULTADO-----')
        print(f'Parada na {j}a iteração')
        print(f'Ljj/L0 = {Lj / L0} < e={e}\n'
              f'Intervalo resultante de x: [{a} {b}]\n'
              f'Intervalo para ymin: [{fun(a)} {fun(b)}]'
              f'END!')
        break
    j = j + 1
    time.sleep(0.1)
    print('\n')
