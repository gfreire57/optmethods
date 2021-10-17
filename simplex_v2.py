"""SIMPLEX - EMA013 Métodos de otimização
Autor: Gabriel Hasmann
Data: 14/10/2021
Atualizado: 16/10/2021
-----------------------------------------------------------"""
from scipy.optimize import linprog
import pandas as pd
import time

print('-> Método da secante')
time.sleep(1)

'''
NECESSÁRIO INSTALAR BIBLIOTECAS SCIPY E PANDAS

A_ub => matriz que contem os elementos das inequações de restrição
b_ub => matriz que contém os valores numericos das inequações de restrição
OBS: pela documentação, as ineqs deverão ser <= ou <

A_eq => matriz que contem os elementos das equações de restrição
b_eq => matriz que contém os valores numéricos das equações de restrição

lb => lower bound / ub => upper bound
(Note that by default lb = 0 and ub = None unless specified with bounds.)
'''

c = [2, 1, -5] #valores da eq a minimizar (inverter valores caso peça para maximizar).
# Alinhar coefs de c com ordem da matriz X.
# P.ex: 1o elem de c refere-se a x1 na equação, o 2o elem refere-se a x2, etc, e ao
# multiplicar A pela matriz X (AX=b), matriz X deve conter elementos na mesma ordem: X= [x1, x2, ...]

A_ub=[[1,  -2, 1],
     [-3, 2,  0],
     [2, 1, -2]]
b_ub = [8, 18, 4]

#INSIRA AQUI OS LABELS DAS VARIÁVEIS QUE SERÃO EXPLORADAS
var = ['x1', 'x2', 'x3']
x_1 = (0, None)
x_2 = (0, None)
x_3 = (0, None)

bounds=(x_1, x_2, x_3)
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds,
              method='simplex',
              options={"disp": True, "presolve": False})

x_1 = res.x[0]
x_2 = res.x[1]
x_3 = res.x[2]

funmin = (-1) * res.fun # VALOR ÓTIMO OBTIDO (se for para maximizar, precisa inverter sinal)
status = res.status
print(f"Foram executadas {res.nit} iterações.")
if  status != 1:
    print("O problema não pôde ser resolvido.\n"
          "Motivo:")
    if status == 1: print(" * Tempo limite atingido.\n")
    if status == 2: print(" * Problema inviável.\n")
    if status == 3: print(" * Problema sem limites bem definidos.\n")
    if status == 4: print(" * Problemas numéricos encontrados.\n")
else:
    print(f"\nValor objetivo é de {funmin:.2f} para a seguinte configuração:\n")
    data = pd.DataFrame([res.x], columns=var)
    print(data)
    #print(f'Xaf:{x_1:.2f} \n Xac:{x_2:.2f} \n Xar:{x_1:.2r} \n Xaf:{x_1:.2f} \n ')

