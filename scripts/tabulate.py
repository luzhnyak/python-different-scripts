#T20_11_v3
#Табулювання функції f на інтервалі [a,b] у n точках
#Використання векторизації або циклу

import numpy as np
from math import sin
#from numpy import sin


def gety(f, x):
    '''Повертає значення функції f для всіх точок з x
    '''
    try:
        y = f(x)
    except Exception as e:
        print('Exception handling', e)
        n = x.size
        y = np.zeros(n)
        for i in range(n):
            y[i] = f(x[i])
    return y



def tabulate(f, a, b, n):
    '''Табулює функцію f на інтервалі [a,b] у n точках
    '''
    x = np.linspace(a, b, n)
    y = gety(f, x)
    return x, y


def fun(x):
    '''x**3 - 7*x - 1
    '''
    return x**3 - 7*x - 1

if __name__ == '__main__':
    n = int(input('Кількість точок: '))
    a = float(input('Початок відрізку: '))
    b = float(input('Кінець відрізку: '))


    funcs = [fun, sin, np.vectorize(sin)]
    for ff in funcs:
        x, y = tabulate(ff, a, b, n)
        if n < 50:
            print('\n', x, '\n', y)
        print('Зроблено для', str(ff))

