import numpy as np
import matplotlib.pyplot as plt
from math import sin
from math import cos

n = 100
a = -10
b = 10

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

x1, y1 = tabulate(sin, a, b, n)
plt.plot(x1, y1) #створити графік
x2, y2 = tabulate(cos, a, b, n)
plt.plot(x2, y2) #створити графік
plt.fill_between(x1, y1, y2)
plt.show()       #показати графік
