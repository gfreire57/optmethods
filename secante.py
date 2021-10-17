"""Secante - EMA013 Métodos de otimização
Autor: Gabriel Hasmann
Data: 15/10/2021
Atualizado: 16/10/2021
-----------------------------------------------------------"""
import time
import sympy as sym

print('-> Método da secante')

# Create symbolic variable x
x = sym.Symbol('x')

'''Valores de entrada e função minimizada'''
# A: ponto inicial
# t0: passo inicial
# e: precisão
# f: função minimizada

A = 0.5
t0 = 0.1
e = 0.001
f = -(1 / (x - 1) ** 2) * (sym.log(x) - 2 * (x - 1) / (x + 1))
# f = 0.1 + 0.1 * x + x ** 2 / (0.1 + x ** 2)

# Differentiate f function
f_dif1 = sym.diff(f, x)  # f_dif são funções simbólicas (não podes ser avaliadas)

# lambdify: Get symb funct and allow it to be evaluated
f_eval = sym.lambdify(x, f)
df = sym.lambdify(x, f_dif1) # df e df2 são as funções que serão avaliadas

# Check 1st derivative of f'(A) and find B
while True:
    df_A = df(A)
    '''if df_A > 0:
        print(f"f'(A) is not negative!!! Get another value.")
        break'''
    df_t0 = df(A + t0)
    # print(f'df_A={df_A}')
    # print(f'df_t0={df_t0}')
    if df_t0 < 0:
        A = A + t0
        t0 = 2*t0
        #print(f'A={A}   t0={t0}\n')
    else:
        B = A + t0
        print('--- Valores de A e B ---')
        print(f"With t0={t0}:\n"
              f"* A={A:.3f} and f'(A)={df(A):.4f}\n"
              f"* B={B:.3f} and f'(B)={df(B):.4f}")
        break
    time.sleep(0.5)

print('\n--> Início das iterações, aguarde...')
time.sleep(0.2)
i = 1
while True and df_A <= 0:
    print(f'\n----IT {i}----')
    xi = A - df(A) * (B - A) / (df(B) - df(A)) # ponto no qual reta secante intersecta eixo x
    print(f'A={A}  |  B={B}')
    print(f'xi = {xi}')
    # Stop criteria
    if abs(df(xi)) <= e:
        print('\n\n\n-----RESULTADO-----')
        print(f"Parada na {i}a iteração\n"
              f"ymin = {f_eval(xi):.3f} onde x={xi:.4f}\n"
              f"|f'(x_i+1)| < e \n"
              f"|{df(xi)}| < {e}")
        break
    elif abs(df(xi)) >= 0:
        B = xi
    elif abs(df(xi)) < 0:
        A = xi

    time.sleep(0.1)
    i += 1