def logarithm(x):
    eps = 0.0000001
    y = 0
    z = 1
    k = 0
    while abs(z) >= eps:
        k = k+1
        z = ((-1)**(k+1))*x**k/k
        y = y+z    
    return y    
while True:
    try:
        x = float(input('введіть x: '))
        assert x > -1 and x < 1, 'x не відповідає заданій умові'
        break
    except AssertionError:
        print('x не відповідає заданій умові')
print(logarithm(x))
