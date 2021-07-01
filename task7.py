from math import factorial


def foo():
    for el in (1, 3, 4, 5, 6, 7, 8):
        yield el


f = foo()

for el in f:
    print(factorial(el))
