"este es mi primer script de python"
GIGANTE = 1000000000000000
PI = 3.141592653589796

def doble(x):
    return 2 * x

def factorial(x):
    r = 1
    if x <= 0:
        return 1
    for i in range(1, x):
        r = r * x
    return r

def power(x, y):
    r = 1
    if y <= 0:
        return 1
    for i in range(0,y):
        r = r * x
    return r

def raizcuadrada(x):
    r = 1
    inc = 1;
    while inc > 1 / GIGANTE:
        while r * r < x:
            r = r + inc
        r = r - inc
        inc = inc / 2
    return r

def mipi(n):
    r = 0
    for i in range(0, n):
        r = r + factorial(4*i)/power(factorial(i), 4)*(26390*i + 1103)/power(396, 4*i)
    r = r * 2 * raizcuadrada(2) / power(99, 2)
    return 1/r

def senaux(x, n):
    r = 0
    for i in range(0, n):
        q = power(x, 2*i+1)/factorial(2*i+1)
        if i % 2 == 0:
            r = r + q
        else:
            r = r - q
    return r

def cosaux(x, n):
    return raizcuadrada(1 - power(senaux(x, n), 2))

def sen(x):
    if x >= 2 * PI:
        return sen(x - 2 * PI)
    elif x >= PI:
        return (-1) * sen(x - PI)
    elif x >= PI/2:
        return sen(PI - x)
    elif x >= PI/4:
        return cosaux(PI/2 - x, 1000)
    else:
        return senaux(x, 1000)
        

