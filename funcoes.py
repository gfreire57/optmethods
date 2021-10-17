import numpy as np
def fib_qelem(x): #x:quantidade de elementos da seq de fibonacci que se deseja
    Fib = np.array([0, 1])
    count = 2
    while len(Fib) <= x+1:
        val = Fib[count-1]+Fib[count-2]
        Fib=np.append(Fib, val)
        count = count+1
    Fib = np.delete(Fib, 0)
    return Fib

def fib_minval(x): #x: valor minimo do maior valor de uma sequencia de fibonacci. Não pega elemento zero
    Fib = np.array([0, 1])
    count = 2
    while max(Fib) < x:
        val = Fib[count-1]+Fib[count-2]
        Fib=np.append(Fib, val)
        count = count+1
    Fib = np.delete(Fib, 0)
    return Fib

print(fib_qelem(6))
print(fib_minval(13))