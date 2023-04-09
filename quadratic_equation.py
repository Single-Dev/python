import math

def quadratic_equation(a, b, c):
    d = b * b - 4 * a * c
    if d==0:
        n=1
        x = int(-b / 2 * a)
    elif d > 0:
        n = 2
        x1 = int((-b + math.pow(d, 0.5)) / 2 * a)
        x2 = int((-b - math.pow(d, 0.5)) / 2 * a)
        x = (x1, x2)
    else:
        return 'empty sum'
    return f'This quadratic equation has {n} solutions and they ({x})'

print(quadratic_equation(1, 4, -12))    