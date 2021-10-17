"""Newton - EMA013 Métodos de otimização
Autor: Gabriel Hasmann
Data: 15/10/2021
Atualizado: 16/10/2021
-----------------------------------------------------------"""
import time
import sympy as sym

print('-> Método de Newton')

'''Cria variável simbólica x'''
x = sym.Symbol('x')

'''Valores de entrada e função minimizada'''
# X1: ponto inicial
# e: precisão
# f: função minimizada

x1 = 0.5
e = 0.001
f = -(1 / (x - 1) ** 2) * (sym.log(x) - 2 * (x - 1) / (x + 1))
# f = 0.1 + 0.1 * x + x ** 2 / (0.1 + x ** 2)

# Diferencia função f
f_dif1 = sym.diff(f, x)  # f_dif são funções simbólicas (não pode ser avaliadas)
f_dif2 = sym.diff(f_dif1,x)
'''sym.pprint(f_dif1, use_unicode=True)
sym.pprint(f_dif2, use_unicode=True)'''

# lambdify: Pega função simbólica e permite ser avaliada
f_eval = sym.lambdify(x, f)
df1 = sym.lambdify(x, f_dif1) # df e df2 são as funções que serão avaliadas
df2 = sym.lambdify(x, f_dif2)

i = 1
xi = x1
while True:
    print(f'----IT {i}----')
    d_f1 = df1(xi)
    d_f2 = df2(xi)
    print(f'xi = {xi}')
    print(f'df1 = {d_f1} | df2 = {d_f2}')
    xi = xi - d_f1 / d_f2
    print(f'xi = {xi}')
    if abs(d_f1) < e:
        print('\n\n\n-----RESULTADO-----')
        print(f"Parada na {i}a iteração\n"
              f"ymin = {f_eval(xi):.3f} onde x={xi:.4f}\n"
              f"|f'(x_i+1)| < e \n"
              f"|{d_f1}| < {e}\n")
        break
    time.sleep(0.1)
    i += 1

# Para visualizar a função derivada simbólica, use os comando abaixo:
'''f_prime = f.diff(x)
pprint(f, use_unicode=True)
pprint(f_prime, use_unicode=True)
'''
